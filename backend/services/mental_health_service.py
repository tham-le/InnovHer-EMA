# services/mental_health_service.py
def get_mental_health_tips(condition):
    return {
        "daily_practices": [
            {
                "title": "Mindfulness meditation",
                "description": "Practice mindfulness for 10-15 minutes daily",
                "benefits": "Reduces stress and anxiety"
            },
            {
                "title": "Gratitude journaling",
                "description": "Write down three things you're grateful for each day",
                "benefits": "Improves mood and outlook"
            }
        ],
        "coping_strategies": [
            {
                "strategy": "Progressive muscle relaxation",
                "description": "Technique to reduce muscle tension and stress"
            },
            {
                "strategy": "Deep breathing exercises",
                "description": "Practice deep breathing when feeling overwhelmed"
            }
        ],
        "support_resources": [
            {
                "type": "Support groups",
                "description": "Join local or online rheumatism support groups"
            },
            {
                "type": "Professional help",
                "description": "Consider talking to a mental health professional"
            }
        ]
    }