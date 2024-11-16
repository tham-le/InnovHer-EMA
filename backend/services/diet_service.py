# services/diet_service.py
def get_diet_recommendations(condition):
    # Placeholder data - in real app, this would come from a database
    return {
        "anti_inflammatory_foods": [
            {"name": "Fatty fish", "benefits": "Rich in omega-3 fatty acids"},
            {"name": "Berries", "benefits": "High in antioxidants"},
            {"name": "Leafy greens", "benefits": "Rich in vitamins and minerals"},
            {"name": "Turmeric", "benefits": "Natural anti-inflammatory properties"}
        ],
        "foods_to_avoid": [
            {"name": "Processed foods", "reason": "Can increase inflammation"},
            {"name": "Sugar", "reason": "May trigger inflammation"},
            {"name": "Red meat", "reason": "Can increase inflammation"}
        ],
        "meal_plan_example": [
            {
                "meal": "Breakfast",
                "suggestion": "Greek yogurt with berries and honey"
            },
            {
                "meal": "Lunch",
                "suggestion": "Salmon salad with leafy greens"
            },
            {
                "meal": "Dinner",
                "suggestion": "Turmeric chicken with vegetables"
            }
        ]
    }

