import re
from deep_translator import LingueeTranslator
import pymorphy2
import nltk
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import operator
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import os

nltk.download('stopwords')

class CareerScoring():
    def __init__(self, path_to_data):
        '''
        Parameters
        ----------
        path_to_data: str
            Path to datasets and models
        '''
        self.stopwords_russian = nltk.corpus.stopwords.words('russian')
        self.morph = pymorphy2.MorphAnalyzer()
        self.translator = LingueeTranslator(source='en', target='ru')

        # load models and datasets
        self.classification_ds = pd.read_csv(
            os.path.join(path_to_data, 'classification_ds.csv'))
        self.combined_offers_ds = pd.read_csv(
            os.path.join(path_to_data, 'combined_offers_ds.csv'))
        with open(os.path.join(path_to_data, 'classification_model.dat'),
                  'rb') as f:
            self.classification_model = pickle.load(f)
        self.spec_codification = pd.read_csv(
            os.path.join(path_to_data, 'spec_codification.csv'))

    def clean_text(self, text, translate=True):
        '''Text cleaning function: remove stop-words, translation if needed,
        lemmatization

        Parameters
        ----------
        text: str
            Text to clean
        translate: bool, default=True
            Translate or not to russian, if translation fails on the side of 
            LingueeTranslator, translation is not applied

        Returns
        ----------
        text: str
            cleaned text
        '''

        def is_russian(text):
            if text is None or len(text) == 0:
                return True
            all_eng = True
            spl = re.split(' |-', text)
            spl = [x for x in spl if x != '']
            if len(spl) == 0:
                return True
            for word in spl:
                if len(word) > 0 and not re.match('[a-z]', word[0]):
                    all_eng = False
            return not all_eng

        def is_intern(pos):
            to_check = ['ассистент', 'стажёр', 'стажировка', 'стажер',
                        'помощник', 'intern']
            for check in to_check:
                if check in pos:
                    return 1, ' '.join(pos.replace(check, '').split())
            return 0, pos

        text = str(text)
        # remove puntuation
        punctuation = '!”$%&\'()*,./:;?@[\]^_`{|}~'
        text = "".join(s for s in text if s not in punctuation)

        text = text.lower()

        text = re.sub('ё', 'е', text)

        # translate to russian
        if translate and not is_russian(text):
            try:
                text = self.translator.translate(text)
            except:
                pass

        tokens = re.split(' |-', text)
        tokens = [token for token in tokens if token != '']

        tokens = [token for token in tokens if
                  token not in self.stopwords_russian]

        # lemmatize
        tokens = [self.morph.parse(token)[0].normal_form for token in tokens]

        tokens = [re.sub('ё', 'е', token) for token in tokens]

        return ' '.join(tokens)

    def get_career_goal(self,
                        jobs,
                        skills,
                        competitions,
                        additional_education,
                        career_area,
                        n_goals=3):
        '''Based on working experience, skills, competitions, education 
        and area of career (if provided) gives a career goal: offer from given dataset

        Parameters
        ----------
        jobs: list of dict
            Job experience
            Keys
                'position', 
                'exp' - working experience, 
                'achievements' - obligations and achievements, would be nice if they are separated with ;
        skills: str or list
            Skills in one string, separated with ',', ';' or '.'
            or
            List of strings
        competitions: list of dict
            List of competitions
            Keys:
                'name' - name of competition
                'achievement' - first place, top-25 etc
        additional_education: list of str
            List of names of courses completed
        career_area: str
            Career area, has high priority in evaluating career goal
            Can be empty string or none - meaning user does not have an area where he/she want to work
        n_goals: int from 1 to 10, default=3
            Number of most accurate career goals returned

        Returns
        ----------
        career_goals: list of str
            List of names of positions - career goals
        '''

        def levenshteinDistance(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            distances = range(len(s1) + 1)
            for i2, c2 in enumerate(s2):
                distances_ = [i2 + 1]
                for i1, c1 in enumerate(s1):
                    if c1 == c2:
                        distances_.append(distances[i1])
                    else:
                        distances_.append(1 + min((distances[i1],
                                                   distances[i1 + 1],
                                                   distances_[-1])))
                distances = distances_
            return distances[-1]

        def get_cosine_similarity(user_skills, offer_skills):
            tfidf = TfidfVectorizer()
            tfidf.fit(user_skills + offer_skills)
            vec_user = tfidf.transform(user_skills)
            vec_offer = tfidf.transform(offer_skills)
            matrix = cosine_similarity(vec_user, vec_offer)
            # maxes = [max(row) for row in matrix]
            return np.mean(matrix)

        if career_area == None or career_area == '':
            job_positions = [j.get('position').lower() for j in jobs]
            specs = self.classification_model.predict(job_positions)
        else:
            scores = {}
            for s in self.spec_codification['specialization'].values:
                scores[s] = 1 - levenshteinDistance(s, career_area)
            specs = sorted(scores.items(), key=operator.itemgetter(1))[-3:]
            specs = [self.spec_codification[
                         self.spec_codification['specialization'] == s][
                         'code'].values[0] for s, _ in specs]

        if type(skills) == str:
            skills = re.split(r';|,|\.', skills)
        user_skills = list(filter(lambda s: s != None and s != '', skills))
        for competition in competitions:
            user_skills.append(
                competition['name'] + ' ' + competition['achievement'])
        for ed in additional_education:
            user_skills.append(ed)
        for job in jobs:
            user_skills.append(job['achievements'])

        if len(user_skills) == 0:
            return [], 'Не удалось определить карьерную цель, вы указали мало данных о себе'

        pos_to_check = self.classification_ds[
            self.classification_ds['specialization'].isin(specs)][
            'position'].values
        offers_to_check = self.combined_offers_ds[
            self.combined_offers_ds['position_lower'].isin(pos_to_check)]

        for skill in user_skills:
            skill = self.clean_text(skill, translate=False)

        max_10 = list(zip([-1.0] * 10, [-1] * 10))
        for index, offer in offers_to_check.iterrows():
            new_sim = get_cosine_similarity(skills, offer['skills'].split(';'))
            max_10.append((new_sim, index))
            max_10 = sorted(max_10)[1:]

        max_10 = list(reversed(list(filter(lambda x: x[1] != -1, max_10))))

        career_goals = [self.combined_offers_ds.iloc[i]['position'] for _, i in
                        max_10[:n_goals]]

        return career_goals, 'Карьерная цель успешно подобрана'
