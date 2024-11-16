# seed.py

from app import app, db
from models import User, Recipe, PainHistory, MoodHistory
from datetime import datetime

def seed_database():
    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        
        print("Creating all tables...")
        db.create_all()
        
        print("Creating sample users...")
        users = [
            User(
                username="john_doe",
                email="john@example.com",
                first_name="John",
                last_name="Doe",
                age=30,
                gender="male",
                height=175.5,
                weight=70.2,
                condition="Rheumatism",
                diagnosed=True,
                allergies="Peanuts",
                medications="Ibuprofen"
            ),
            User(
                username="jane_smith",
                email="jane@example.com",
                first_name="Jane",
                last_name="Smith",
                age=25,
                gender="female",
                height=165.0,
                weight=58.5,
                condition="Arthritis",
                diagnosed=True,
                allergies="None",
                medications="Vitamin D"
            )
        ]
        db.session.add_all(users)
        db.session.commit()
        
        print("Creating sample recipes...")
        recipes = [
            Recipe(
                name="Anti-Inflammatory Smoothie",
                ingredients="1 cup blueberries, 1 banana, 1 tsp turmeric, 1 cup almond milk",
                instructions="Blend all ingredients until smooth. Serve immediately.",
                image_url="smoothie.jpg",
                type="breakfast"
            ),
            Recipe(
                name="Salmon with Vegetables",
                ingredients="Salmon fillet, broccoli, carrots, olive oil",
                instructions="Bake salmon and roast vegetables with olive oil.",
                image_url="salmon.jpg",
                type="dinner"
            ),
            Recipe(
                name="Quinoa Salad",
                ingredients="Quinoa, cucumber, tomatoes, olive oil",
                instructions="Mix cooked quinoa with vegetables and dress with olive oil.",
                image_url="quinoa.jpg",
                type="lunch"
            )
        ]
        db.session.add_all(recipes)
        db.session.commit()
        
        print("Creating pain history records...")
        pain_records = [
            PainHistory(
                user_id=1,
                pain_level=5,
                pain_type="joint",
                description="Morning stiffness in knees"
            ),
            PainHistory(
                user_id=1,
                pain_level=3,
                pain_type="muscle",
                description="Slight discomfort after walking"
            )
        ]
        db.session.add_all(pain_records)
        
        print("Creating mood history records...")
        mood_records = [
            MoodHistory(
                user_id=1,
                mood="happy",
                mood_description="Feeling good after exercise"
            ),
            MoodHistory(
                user_id=1,
                mood="tired",
                mood_description="Fatigue in the evening"
            )
        ]
        db.session.add_all(mood_records)
        
        # Add some favorite recipes for users
        users[0].favorite_recipes.extend([recipes[0], recipes[1]])
        users[1].favorite_recipes.append(recipes[2])
        
        db.session.commit()
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()