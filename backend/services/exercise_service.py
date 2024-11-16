# services/exercise_service.py
def get_exercise_recommendations(condition):
    return {
        "low_impact_exercises": [
            {
                "name": "Water aerobics",
                "benefits": "Reduces joint stress, improves flexibility",
                "duration": "30 minutes",
                "frequency": "3 times per week"
            },
            {
                "name": "Gentle yoga",
                "benefits": "Increases flexibility, reduces stiffness",
                "duration": "20-30 minutes",
                "frequency": "Daily"
            },
            {
                "name": "Walking",
                "benefits": "Improves cardiovascular health, maintains joint mobility",
                "duration": "20 minutes",
                "frequency": "Daily"
            }
        ],
        "stretching_exercises": [
            {
                "name": "Joint mobility exercises",
                "instructions": "Gentle rotation of major joints",
                "duration": "10 minutes",
                "frequency": "Twice daily"
            }
        ],
        "precautions": [
            "Avoid high-impact activities",
            "Stop if pain increases",
            "Start slowly and gradually increase intensity"
        ]
    }

