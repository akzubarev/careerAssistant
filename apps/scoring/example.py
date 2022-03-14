from scoring_model import CareerScoring

if __name__ == "__main__":
    scoring = CareerScoring('../../data/')
    goals = scoring.get_career_goal(
        jobs=[{
            'position': 'веб-дизайнер',
            'exp': 24,
            'achievements': 'работал в Adobe Photoshop'
        }],
        skills='Adobe Photoshop, Figma, теория ui/ux дизайна, python начальный уровень, HTML, CSS',
        competitions=[],
        additional_education=['Введение в веб-дизайн', 'Figma'],
        career_area=None,
        n_goals=5
    )
    print(goals)
