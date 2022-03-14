import pandas as pd
import os
import re
from transformers import BertTokenizer, BertForTokenClassification
from keras.preprocessing.sequence import pad_sequences
from sklearn.metrics.pairwise import cosine_similarity


BERT_PATH = 'sberbank-ai/ruBert-base'
SPLIT_BY = r"[\w']+|[«»\",.?!;]"


def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


class RecommendationSystem:
    def __init__(self, path_to_data : str):
        '''
        Parameters
        ----------
        path_to_data: str
            Path to datasets.
        '''

        self.tokenizer = None

        # Swapping datasets.
        self.new_job = pd.read_csv(os.path.join(path_to_data, 'jobs_for_articles.csv'))
        self.jobs = pd.read_csv(os.path.join(path_to_data, 'vacances.csv'))
        self.favorites = pd.read_csv(os.path.join(path_to_data, 'favorites_for_articles.csv'))
        self.spec_codification = pd.read_csv(os.path.join(path_to_data, 'spec_codification.csv'))
        self.classification_ds = pd.read_csv(os.path.join(path_to_data, 'classification_ds.csv'))

    def _get_n_top_scoring(self, n_scoring : int = 3, scoring_result : list = []):
        '''
        Select the first few examples from the scoring results.

        Parameters
        ----------
        n_scoring: int
            Number of examples to be cut.
        scoring_result: list
            Result of scoring system.
        '''

        return [word.lower() for word in scoring_result[:n_scoring]]

    def recommend_vacancies(
        self,
        n_scoring : int = 3,
        n_specializations : int = 2,
        n_vacances_on_specialization : int = 1,
        scoring_result : list = []
    ):
        '''
        Returns relevant vacancies based on scoring results.

        Parameters
        ----------
        n_scoring: int
            Number of examples to be cut.
        n_specializations: int
            The number of specializations for each of the scoring examples.
        n_vacances_on_specialization: int
            The number of selected vacancies for each specialization.
        scoring_result: list
            Result of scoring system.

        Return Value
        ----------
        vacances: list
            List of vacancies, where each vacancy is represented by a dictionary
                of the 'Название' and 'Компания'.
        '''

        best_result_scoring = self._get_n_top_scoring(n_scoring = n_scoring, scoring_result = scoring_result)
        vacances = []

        for prof in best_result_scoring:
            professional_codes = list(
                self.classification_ds.loc[self.classification_ds['position'] == prof]['specialization']
            )[:n_specializations]
            specializations = []

            for code in professional_codes:
                specializations.extend(
                    list(self.spec_codification.loc[self.spec_codification['code'] == code]['specialization'])
                )

            for spec in specializations:
                try:
                    frame_vacances = self.jobs.loc[self.jobs['Профессия'] == spec].sample(n = n_vacances_on_specialization)
                except ValueError:
                    continue

                if frame_vacances.shape[0] > 1:
                    for frame_vacancy in frame_vacances:
                        vacances.append({'Название' : frame_vacances.iloc[0, 0], 'Компания' : frame_vacances.iloc[0, 1].rpartition('[')[0]})
                else:
                    vacances.append({'Название' : frame_vacances.iloc[0, 0], 'Компания' : frame_vacances.iloc[0, 1].rpartition('[')[0]})

        if len(vacances) == 0:
            distances = []
            goal = best_result_scoring[0]

            for index, row in self.spec_codification.iterrows():
                error_local = levenshteinDistance(goal, row['specialization'])
                distances.append((row['specialization'], error_local))
            
            distances = sorted(distances, key=lambda x: x[1], reverse=True)
            taken_vacancies_m = 0

            for distance in distances:
                try:
                    frame_vacances = self.jobs.loc[self.jobs['Профессия'] == distance[0]].sample(n = n_vacances_on_specialization)
                except ValueError:
                    continue

                if frame_vacances.shape[0] > 1:
                    for frame_vacancy in frame_vacances:
                        vacances.append({'Название' : frame_vacances.iloc[0, 0], 'Компания' : frame_vacances.iloc[0, 1].rpartition('[')[0]})
                else:
                    vacances.append({'Название' : frame_vacances.iloc[0, 0], 'Компания' : frame_vacances.iloc[0, 1].rpartition('[')[0]})

                taken_vacancies_m += frame_vacances.shape[0]
                if taken_vacancies_m >= n_vacances_on_specialization:
                    vacances = vacances[:n_vacances_on_specialization]
                    break

        return vacances

    def _to_tokenized(self, text : str = ''):
        '''
        Transform text to embiddings.

        Parameters
        ----------
        text: list
            Text for transformation.
        '''

        tokens =  re.findall(SPLIT_BY, text.lower())
        bert_tokens = []
        for word in tokens:
            bert_tokens.extend(self.tokenizer.tokenize(word))

        ids_tokens = [self.tokenizer.convert_tokens_to_ids(word) for word in bert_tokens]
        ids_tokens = pad_sequences(
            [ids_tokens],
            maxlen=128,
            dtype="long",
            value=0.0,
            truncating="post",
            padding="post",
        )
        return ids_tokens

    def recommend_articles(self, max_n_articles : int = 3, skills : str = ''):
        '''
        Returns articles based on collaborative filtering with cosine similarity.

        Parameters
        ----------
        max_n_articles: int
            The maximum of articles that the recommended source can return.
            Note: The number of articles may be less than this variable.
        skills: str
            Skills or experience in one string.

        Return Value
        ----------
        articles: list
            List of articles, where each vacancy is represented by string.
        '''

        print('BertTokeziner activate...')
        self.tokenizer = BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=False)

        articles = []
        tokenized_skills = self._to_tokenized(skills)
        self.new_job['text'] = self.new_job['text'].apply(lambda x: self._to_tokenized(x))

        distances = []

        for index, row in self.new_job.iterrows():
            error_local = cosine_similarity(tokenized_skills, row['text'])
            distances.append((row['User ID'], error_local))

        distances = sorted(distances, key=lambda x: x[1], reverse=True)
        taken_articles_m = 0

        for distance in distances:
            new_sources = list(
                self.favorites.loc[self.favorites['User ID'].isin([distance[0]])]['Название'][self.favorites['Тип объекта'] == 'Статья']
            )
            articles.extend(new_sources)
            taken_articles_m += len(new_sources)

            if taken_articles_m >= max_n_articles:
                taken_articles_m = articles[:max_n_articles]
                break

        return articles
