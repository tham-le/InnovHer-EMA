# seed.py

from app import app, db
from models import User, Recipe, PainHistory, MoodHistory
from datetime import datetime
import json

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
                    name="Tartare de saumon et avocat",
                    ingredients=json.dumps([
                        {
                            "quantity": 150,
                            "unit": "g",
                            "item": "saumon frais",
                            "details": "(surgelé puis décongelé)"
                        },
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "avocat",
                            "details": ""
                        },
                        {
                            "quantity": 1,
                            "unit": "cuillère à soupe",
                            "item": "jus de citron",
                            "details": ""
                        },
                        {
                            "quantity": 1,
                            "unit": "cuillère à soupe",
                            "item": "huile d'olive",
                            "details": ""
                        },
                        {
                            "quantity": None,
                            "unit": "",
                            "item": "sel",
                            "details": ""
                        },
                        {
                            "quantity": None,
                            "unit": "",
                            "item": "poivre",
                            "details": ""
                        },
                        {
                            "quantity": None,
                            "unit": "",
                            "item": "aneth frais",
                            "details": ""
                        }
                    ]),
                    instructions=json.dumps([
                        "Couper le saumon en petits dés.",
                        "Couper l'avocat en dés et mélanger avec le jus de citron.",
                        "Ajouter le saumon, l'huile d'olive, le sel, le poivre et l'aneth.",
                        "Mélanger doucement et servir frais."
                    ]),
                    image_url="tartare.jpg",
                    type="lunch"
                ),
                Recipe(
                    name="Anti-Inflammatory Smoothie",
                    ingredients=json.dumps([
                        {
                            "quantity": 1,
                            "unit": "cup",
                            "item": "blueberries",
                            "details": "fresh or frozen"
                        },
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "banana",
                            "details": "ripe"
                        },
                        {
                            "quantity": 1,
                            "unit": "tsp",
                            "item": "turmeric",
                            "details": "ground"
                        },
                        {
                            "quantity": 1,
                            "unit": "cup",
                            "item": "almond milk",
                            "details": ""
                        }
                    ]),
                    instructions=json.dumps([
                        "Add all ingredients to blender.",
                        "Blend until smooth.",
                        "Serve immediately."
                    ]),
                    image_url="smoothie.jpg",
                    type="breakfast"
                ),
                Recipe(
                    name="Quinoa Bowl with Roasted Vegetables",
                    ingredients=json.dumps([
                        {
                            "quantity": 100,
                            "unit": "g",
                            "item": "quinoa",
                            "details": "rinsed"
                        },
                        {
                            "quantity": 200,
                            "unit": "g",
                            "item": "mixed vegetables",
                            "details": "(butternut squash, zucchini, carrots)"
                        },
                        {
                            "quantity": 2,
                            "unit": "tablespoon",
                            "item": "olive oil",
                            "details": "extra virgin"
                        },
                        {
                            "quantity": 50,
                            "unit": "g",
                            "item": "pumpkin seeds",
                            "details": "raw"
                        },
                        {
                            "quantity": None,
                            "unit": "",
                            "item": "fresh herbs",
                            "details": "(thyme, rosemary)"
                        }
                    ]),
                    instructions=json.dumps([
                        "Rinse quinoa thoroughly and cook in water until fluffy",
                        "Cut vegetables into similar-sized pieces",
                        "Toss vegetables with 1 tbsp olive oil and herbs",
                        "Gently roast vegetables at low temperature (150°C) for 25-30 minutes",
                        "Combine quinoa and vegetables, drizzle with remaining olive oil",
                        "Top with pumpkin seeds and serve"
                    ]),
                    image_url="quinoa_bowl.jpg",
                    type="lunch"
                ),
                Recipe(
                    name="Wild-Caught Fish with Fresh Herbs",
                    ingredients=json.dumps([
                        {
                            "quantity": 200,
                            "unit": "g",
                            "item": "wild sea bass",
                            "details": "fresh fillet"
                        },
                        {
                            "quantity": 1,
                            "unit": "bunch",
                            "item": "fresh parsley",
                            "details": ""
                        },
                        {
                            "quantity": 1,
                            "unit": "lemon",
                            "item": "organic lemon",
                            "details": "juice and zest"
                        },
                        {
                            "quantity": 2,
                            "unit": "tablespoon",
                            "item": "olive oil",
                            "details": "extra virgin"
                        },
                        {
                            "quantity": 200,
                            "unit": "g",
                            "item": "green beans",
                            "details": "fresh"
                        }
                    ]),
                    instructions=json.dumps([
                        "Season fish with herbs, lemon zest, and olive oil",
                        "Steam green beans until tender-crisp",
                        "Gently cook fish at low temperature",
                        "Serve with steamed green beans and lemon juice"
                    ]),
                    image_url="fish.jpg",
                    type="dinner"
                ),
                Recipe(
                    name="Berry and Almond Breakfast Bowl",
                    ingredients=json.dumps([
                        {
                            "quantity": 150,
                            "unit": "g",
                            "item": "mixed berries",
                            "details": "fresh or frozen"
                        },
                        {
                            "quantity": 30,
                            "unit": "g",
                            "item": "almonds",
                            "details": "raw"
                        },
                        {
                            "quantity": 1,
                            "unit": "tablespoon",
                            "item": "honey",
                            "details": "raw, optional"
                        },
                        {
                            "quantity": 200,
                            "unit": "ml",
                            "item": "almond milk",
                            "details": "unsweetened"
                        }
                    ]),
                    instructions=json.dumps([
                        "Combine berries in a bowl",
                        "Roughly chop almonds",
                        "Pour almond milk over berries",
                        "Top with chopped almonds and honey if desired"
                    ]),
                    image_url="berry_bowl.jpg",
                    type="breakfast"
                ),
                Recipe(
                    name="Sweet Potato and Avocado Salad",
                    ingredients=json.dumps([
                        {
                            "quantity": 1,
                            "unit": "large",
                            "item": "sweet potato",
                            "details": "peeled and cubed"
                        },
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "avocado",
                            "details": "ripe"
                        },
                        {
                            "quantity": 100,
                            "unit": "g",
                            "item": "mixed greens",
                            "details": "fresh"
                        },
                        {
                            "quantity": 2,
                            "unit": "tablespoon",
                            "item": "olive oil",
                            "details": "extra virgin"
                        },
                        {
                            "quantity": 1,
                            "unit": "tablespoon",
                            "item": "lemon juice",
                            "details": "fresh"
                        }
                    ]),
                    instructions=json.dumps([
                        "Steam sweet potato cubes until tender",
                        "Slice avocado",
                        "Arrange mixed greens on plate",
                        "Top with sweet potato and avocado",
                        "Drizzle with olive oil and lemon juice"
                    ]),
                    image_url="sweet_potato_salad.jpg",
                    type="lunch"
                ),
                Recipe(
                    name="Herb-Roasted Turkey with Vegetables",
                    ingredients=json.dumps([
                        {
                            "quantity": 200,
                            "unit": "g",
                            "item": "turkey breast",
                            "details": "organic"
                        },
                        {
                            "quantity": 300,
                            "unit": "g",
                            "item": "mixed root vegetables",
                            "details": "(carrots, parsnips, turnips)"
                        },
                        {
                            "quantity": 2,
                            "unit": "tablespoon",
                            "item": "olive oil",
                            "details": "extra virgin"
                        },
                        {
                            "quantity": 1,
                            "unit": "bunch",
                            "item": "fresh herbs",
                            "details": "(sage, thyme, rosemary)"
                        }
                    ]),
                    instructions=json.dumps([
                        "Season turkey with herbs and olive oil",
                        "Prepare vegetables and toss with olive oil",
                        "Roast turkey and vegetables at low temperature (150°C)",
                        "Let rest before serving"
                    ]),
                    image_url="turkey.jpg",
                    type="dinner"
                ),
                Recipe(
                    name="Tropical Morning Smoothie",
                    ingredients=json.dumps([
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "mango",
                            "details": "ripe"
                        },
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "banana",
                            "details": "ripe"
                        },
                        {
                            "quantity": 200,
                            "unit": "ml",
                            "item": "coconut water",
                            "details": "fresh"
                        },
                        {
                            "quantity": 1,
                            "unit": "thumb",
                            "item": "ginger",
                            "details": "fresh"
                        }
                    ]),
                    instructions=json.dumps([
                        "Peel and chop mango and banana",
                        "Grate ginger",
                        "Blend all ingredients until smooth",
                        "Serve immediately"
                    ]),
                    image_url="tropical_smoothie.jpg",
                    type="breakfast"
                ),
                Recipe(
                    name="Mediterranean Salmon Salad",
                    ingredients=json.dumps([
                        {
                            "quantity": 150,
                            "unit": "g",
                            "item": "wild salmon",
                            "details": "fresh"
                        },
                        {
                            "quantity": 100,
                            "unit": "g",
                            "item": "mixed salad leaves",
                            "details": "fresh"
                        },
                        {
                            "quantity": 50,
                            "unit": "g",
                            "item": "olives",
                            "details": "kalamata"
                        },
                        {
                            "quantity": 2,
                            "unit": "tablespoon",
                            "item": "olive oil",
                            "details": "extra virgin"
                        },
                        {
                            "quantity": 1,
                            "unit": "",
                            "item": "lemon",
                            "details": "juice only"
                        }
                    ]),
                    instructions=json.dumps([
                        "Gently cook salmon at low temperature",
                        "Prepare salad leaves and olives",
                        "Flake salmon and arrange over salad",
                        "Dress with olive oil and lemon juice"
                    ]),
                    image_url="salmon_salad.jpg",
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
        
        db.session.commit()
        print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
    # load_recipes()