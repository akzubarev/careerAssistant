from recommendation_system import RecommendationSystem

if __name__ == "__main__":
    SCORING_RESULT = ['Тестировщик', 'Web-программист',
                      'Помощник технического директора / администратор сайтов / разработчик',
                      'QA специалист (тестировщик)', 'QA Automation']
    EXPERIENCE = 'McKinsey Младший консультант Консалтинг'

    recommender = RecommendationSystem('../../data/')

    vacances = recommender.recommend_vacancies(scoring_result=SCORING_RESULT)
    articles = recommender.recommend_articles(skills=EXPERIENCE)
    print(vacances)
    print(articles)