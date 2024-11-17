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
    name="Saumon aux Herbes de Provence",
    ingredients=json.dumps([
        {
            "quantity": 200,
            "unit": "g",
            "item": "saumon sauvage",
            "details": "filet frais"
        },
        {
            "quantity": 1,
            "unit": "cuillère à soupe",
            "item": "herbes de Provence",
            "details": "séchées"
        },
        {
            "quantity": 2,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 200,
            "unit": "g",
            "item": "épinards",
            "details": "frais"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "noix",
            "details": "concassées"
        }
    ]),
    instructions=json.dumps([
        "Préchauffer le four à 180°C",
        "Assaisonner le saumon avec les herbes et l'huile d'olive",
        "Cuire au four pendant 15-20 minutes",
        "Faire revenir les épinards à l'huile d'olive",
        "Garnir de noix concassées"
    ]),
    image_url="salmon.jpg",
    type="dinner"
),

Recipe(
    name="Petit-déjeuner Méditerranéen",
    ingredients=json.dumps([
        {
            "quantity": 150,
            "unit": "g",
            "item": "yaourt grec",
            "details": "nature"
        },
        {
            "quantity": 30,
            "unit": "g",
            "item": "amandes",
            "details": "effilées"
        },
        {
            "quantity": 100,
            "unit": "g",
            "item": "myrtilles",
            "details": "fraîches"
        },
        {
            "quantity": 1,
            "unit": "cuillère à café",
            "item": "miel",
            "details": "bio"
        }
    ]),
    instructions=json.dumps([
        "Verser le yaourt dans un bol",
        "Ajouter les myrtilles",
        "Saupoudrer d'amandes",
        "Napper de miel"
    ]),
    image_url="breakfast.jpg",
    type="breakfast"
),

# Mardi
Recipe(
    name="Salade de Quinoa aux Légumineuses",
    ingredients=json.dumps([
        {
            "quantity": 150,
            "unit": "g",
            "item": "quinoa",
            "details": "cuit"
        },
        {
            "quantity": 100,
            "unit": "g",
            "item": "pois chiches",
            "details": "cuits"
        },
        {
            "quantity": 100,
            "unit": "g",
            "item": "tomates cerises",
            "details": "coupées en deux"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "olives kalamata",
            "details": "dénoyautées"
        },
        {
            "quantity": 3,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        }
    ]),
    instructions=json.dumps([
        "Mélanger le quinoa cuit avec les pois chiches",
        "Ajouter les tomates et les olives",
        "Assaisonner avec l'huile d'olive",
        "Servir à température ambiante"
    ]),
    image_url="quinoa_salad.jpg",
    type="lunch"
),

# Continue with the rest of the week...
# Each day includes breakfast, lunch, and dinner recipes following the same format
# Focusing on anti-inflammatory ingredients like:
# - Fatty fish (salmon, sardines, maquereau)
# - Whole grains (quinoa, riz complet)
# - Legumes (lentilles, pois chiches)
# - Nuts and seeds (noix, amandes, graines de lin)
# - Olive oil
# - Fresh fruits and vegetables
# - Mediterranean herbs and spices

# Mercredi
Recipe(
    name="Sardines Grillées aux Herbes",
    ingredients=json.dumps([
        {
            "quantity": 300,
            "unit": "g",
            "item": "sardines fraîches",
            "details": "nettoyées"
        },
        {
            "quantity": 2,
            "unit": "citrons",
            "item": "citrons bio",
            "details": "en quartiers"
        },
        {
            "quantity": 1,
            "unit": "bouquet",
            "item": "persil frais",
            "details": "haché"
        }
    ]),
    instructions=json.dumps([
        "Assaisonner les sardines avec les herbes",
        "Griller 3-4 minutes de chaque côté",
        "Servir avec les quartiers de citron"
    ]),
    image_url="sardines.jpg",
    type="dinner"
),
# Lundi
Recipe(
    name="Pavé de Saumon aux Agrumes et Fenouil",
    ingredients=json.dumps([
        {
            "quantity": 180,
            "unit": "g",
            "item": "saumon sauvage",
            "details": "pavé frais"
        },
        {
            "quantity": 1,
            "unit": "bulbe",
            "item": "fenouil",
            "details": "émincé finement"
        },
        {
            "quantity": 1,
            "unit": "orange",
            "item": "orange bio",
            "details": "en segments"
        },
        {
            "quantity": 2,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 1,
            "unit": "pincée",
            "item": "graines de fenouil",
            "details": "écrasées"
        }
    ]),
    instructions=json.dumps([
        "Préchauffer le four à 180°C",
        "Disposer le fenouil émincé dans un plat",
        "Poser le saumon dessus",
        "Arroser d'huile d'olive et parsemer de graines de fenouil",
        "Cuire 18-20 minutes",
        "Garnir avec les segments d'orange avant de servir"
    ]),
    image_url="salmon_fennel.jpg",
    type="dinner"
),

Recipe(
    name="Salade Tiède de Lentilles Vertes aux Noix",
    ingredients=json.dumps([
        {
            "quantity": 200,
            "unit": "g",
            "item": "lentilles vertes du Puy",
            "details": "crues"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "noix",
            "details": "torréfiées et concassées"
        },
        {
            "quantity": 1,
            "unit": "échalote",
            "item": "échalote",
            "details": "ciselée finement"
        },
        {
            "quantity": 3,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 1,
            "unit": "bouquet",
            "item": "persil plat",
            "details": "frais haché"
        }
    ]),
    instructions=json.dumps([
        "Cuire les lentilles dans l'eau bouillante 20-25 minutes",
        "Égoutter et laisser tiédir",
        "Mélanger avec l'échalote et le persil",
        "Arroser d'huile d'olive",
        "Parsemer de noix concassées"
    ]),
    image_url="lentils.jpg",
    type="lunch"
),

# Mardi
Recipe(
    name="Daurade en Croûte d'Herbes",
    ingredients=json.dumps([
        {
            "quantity": 200,
            "unit": "g",
            "item": "filet de daurade",
            "details": "frais"
        },
        {
            "quantity": 1,
            "unit": "bouquet",
            "item": "mélange d'herbes fraîches",
            "details": "basilic, persil, ciboulette"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "amandes",
            "details": "effilées"
        },
        {
            "quantity": 2,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 200,
            "unit": "g",
            "item": "haricots verts",
            "details": "fins"
        }
    ]),
    instructions=json.dumps([
        "Mixer les herbes avec les amandes et l'huile d'olive",
        "Recouvrir le poisson de ce mélange",
        "Cuire au four 15 minutes à 180°C",
        "Servir avec les haricots verts vapeur"
    ]),
    image_url="seabream.jpg",
    type="dinner"
),

# Mercredi
Recipe(
    name="Bowl de Quinoa aux Légumes Rôtis et Pois Chiches",
    ingredients=json.dumps([
        {
            "quantity": 150,
            "unit": "g",
            "item": "quinoa",
            "details": "bien rincé"
        },
        {
            "quantity": 400,
            "unit": "g",
            "item": "légumes racines",
            "details": "patate douce, carotte, panais"
        },
        {
            "quantity": 200,
            "unit": "g",
            "item": "pois chiches",
            "details": "cuits"
        },
        {
            "quantity": 1,
            "unit": "cuillère à café",
            "item": "curcuma",
            "details": "en poudre"
        },
        {
            "quantity": 3,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "graines de courge",
            "details": "torréfiées"
        }
    ]),
    instructions=json.dumps([
        "Cuire le quinoa selon les instructions",
        "Rôtir les légumes avec le curcuma et l'huile d'olive",
        "Réchauffer les pois chiches",
        "Assembler le bowl : quinoa, légumes, pois chiches",
        "Parsemer de graines de courge"
    ]),
    image_url="quinoa_bowl.jpg",
    type="dinner"
),

# Jeudi
Recipe(
    name="Maquereau Grillé à la Provençale",
    ingredients=json.dumps([
        {
            "quantity": 200,
            "unit": "g",
            "item": "filets de maquereau",
            "details": "frais"
        },
        {
            "quantity": 400,
            "unit": "g",
            "item": "ratatouille",
            "details": "aubergines, courgettes, poivrons, tomates"
        },
        {
            "quantity": 2,
            "unit": "gousses",
            "item": "ail",
            "details": "émincées"
        },
        {
            "quantity": 1,
            "unit": "citron",
            "item": "citron bio",
            "details": "en quartiers"
        },
        {
            "quantity": 1,
            "unit": "bouquet",
            "item": "herbes de Provence",
            "details": "thym, romarin, origan"
        }
    ]),
    instructions=json.dumps([
        "Préparer la ratatouille traditionnelle",
        "Assaisonner les maquereaux d'herbes et d'ail",
        "Griller les maquereaux 3-4 minutes de chaque côté",
        "Servir sur un lit de ratatouille",
        "Accompagner de quartiers de citron"
    ]),
    image_url="mackerel_provencal.jpg",
    type="dinner"
),

# Vendredi
Recipe(
    name="Soupe de Poisson aux Légumes Méditerranéens",
    ingredients=json.dumps([
        {
            "quantity": 300,
            "unit": "g",
            "item": "poisson blanc",
            "details": "cabillaud ou lotte"
        },
        {
            "quantity": 1,
            "unit": "boîte",
            "item": "tomates concassées",
            "details": "400g"
        },
        {
            "quantity": 2,
            "unit": "poireaux",
            "item": "poireaux",
            "details": "émincés"
        },
        {
            "quantity": 2,
            "unit": "branches",
            "item": "céleri",
            "details": "émincées"
        },
        {
            "quantity": 1,
            "unit": "pincée",
            "item": "safran",
            "details": "en poudre"
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "pistaches",
            "details": "non salées, concassées"
        }
    ]),
    instructions=json.dumps([
        "Faire revenir les légumes à l'huile d'olive",
        "Ajouter les tomates et le safran",
        "Couvrir d'eau et laisser mijoter 20 minutes",
        "Ajouter le poisson et cuire 5 minutes",
        "Servir parsemé de pistaches"
    ]),
    image_url="fish_soup.jpg",
    type="dinner"
),
Recipe(
    name="Porridge aux Fruits Rouges et Graines",
    ingredients=json.dumps([
        {
            "quantity": 50,
            "unit": "g",
            "item": "flocons d'avoine",
            "details": "sans gluten"
        },
        {
            "quantity": 200,
            "unit": "ml",
            "item": "lait d'amande",
            "details": "non sucré"
        },
        {
            "quantity": 100,
            "unit": "g",
            "item": "fruits rouges",
            "details": "frais ou surgelés"
        },
        {
            "quantity": 1,
            "unit": "cuillère à soupe",
            "item": "graines de chia",
            "details": ""
        },
        {
            "quantity": 1,
            "unit": "cuillère à café",
            "item": "miel",
            "details": "bio"
        },
        {
            "quantity": 1,
            "unit": "pincée",
            "item": "cannelle",
            "details": "en poudre"
        }
    ]),
    instructions=json.dumps([
        "Faire chauffer le lait d'amande",
        "Ajouter les flocons d'avoine et les graines de chia",
        "Cuire à feu doux 5 minutes en remuant",
        "Ajouter les fruits rouges et la cannelle",
        "Napper de miel"
    ]),
    image_url="porridge.jpg",
    type="breakfast"
),

Recipe(
    name="Toast à l'Avocat et Saumon Fumé",
    ingredients=json.dumps([
        {
            "quantity": 2,
            "unit": "tranches",
            "item": "pain complet au levain",
            "details": "grillé"
        },
        {
            "quantity": 1,
            "unit": "fruit",
            "item": "avocat",
            "details": "mûr"
        },
        {
            "quantity": 80,
            "unit": "g",
            "item": "saumon fumé",
            "details": "sauvage"
        },
        {
            "quantity": 1,
            "unit": "citron",
            "item": "citron bio",
            "details": "pour le jus"
        },
        {
            "quantity": 1,
            "unit": "poignée",
            "item": "graines de lin",
            "details": "moulues"
        }
    ]),
    instructions=json.dumps([
        "Écraser l'avocat avec le jus de citron",
        "Griller le pain",
        "Étaler l'avocat sur le pain",
        "Disposer le saumon fumé",
        "Parsemer de graines de lin"
    ]),
    image_url="avocado_toast.jpg",
    type="breakfast"
),
Recipe(
    name="Smoothie Bowl Anti-inflammatoire",
    ingredients=json.dumps([
        {
            "quantity": 1,
            "unit": "fruit",
            "item": "mangue",
            "details": "surgelée"
        },
        {
            "quantity": 1,
            "unit": "banane",
            "item": "banane",
            "details": "surgelée"
        },
        {
            "quantity": 2,
            "unit": "cm",
            "item": "gingembre frais",
            "details": "pelé"
        },
        {
            "quantity": 1,
            "unit": "cuillère à café",
            "item": "curcuma",
            "details": "frais ou en poudre"
        },
        {
            "quantity": 200,
            "unit": "ml",
            "item": "lait de coco",
            "details": "bio"
        },
        {
            "quantity": 20,
            "unit": "g",
            "item": "granola sans gluten",
            "details": "pour le topping"
        },
        {
            "quantity": 1,
            "unit": "cuillère à soupe",
            "item": "noix de coco",
            "details": "râpée"
        }
    ]),
    instructions=json.dumps([
        "Mixer les fruits surgelés avec le lait de coco",
        "Ajouter le gingembre et le curcuma",
        "Verser dans un bol",
        "Garnir de granola et noix de coco"
    ]),
    image_url="smoothie_bowl.jpg",
    type="breakfast"
),

Recipe(
    name="Omelette Méditerranéenne aux Herbes",
    ingredients=json.dumps([
        {
            "quantity": 3,
            "unit": "unités",
            "item": "œufs bio",
            "details": ""
        },
        {
            "quantity": 50,
            "unit": "g",
            "item": "épinards frais",
            "details": ""
        },
        {
            "quantity": 2,
            "unit": "cuillères à soupe",
            "item": "huile d'olive",
            "details": "extra vierge"
        },
        {
            "quantity": 1,
            "unit": "bouquet",
            "item": "herbes fraîches",
            "details": "basilic, ciboulette, persil"
        },
        {
            "quantity": 30,
            "unit": "g",
            "item": "fromage de chèvre frais",
            "details": "facultatif"
        }
    ]),
    instructions=json.dumps([
        "Battre les œufs avec les herbes ciselées",
        "Faire revenir les épinards à l'huile d'olive",
        "Verser les œufs battus",
        "Cuire doucement et ajouter le fromage",
        "Plier l'omelette et servir"
    ]),
    image_url="omelette.jpg",
    type="breakfast"
),
Recipe(
    name="Chia Pudding aux Fruits d'Été",
    ingredients=json.dumps([
        {
            "quantity": 4,
            "unit": "cuillères à soupe",
            "item": "graines de chia",
            "details": ""
        },
        {
            "quantity": 250,
            "unit": "ml",
            "item": "lait végétal",
            "details": "amande ou avoine"
        },
        {
            "quantity": 100,
            "unit": "g",
            "item": "pêches",
            "details": "fraîches"
        },
        {
            "quantity": 1,
            "unit": "cuillère à café",
            "item": "extrait de vanille",
            "details": "pure"
        },
        {
            "quantity": 2,
            "unit": "cuillères à soupe",
            "item": "amandes effilées",
            "details": "grillées"
        }
    ]),
    instructions=json.dumps([
        "Mélanger les graines de chia avec le lait et la vanille",
        "Laisser reposer au frais toute la nuit",
        "Le matin, couper les pêches en dés",
        "Disposer les fruits sur le pudding",
        "Parsemer d'amandes grillées"
    ]),
    image_url="chia_pudding.jpg",
    type="breakfast"
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