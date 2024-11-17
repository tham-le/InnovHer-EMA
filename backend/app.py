from flask import Flask, jsonify, request
from flask_cors import CORS
from models import (
    db, User, Recipe, PainHistory, MoodHistory,
    UserSchema, PainHistorySchema, MoodHistorySchema, RecipeSchema,
    MealPlan, MealPlanSchema
)
from marshmallow import ValidationError
import os
from dotenv import load_dotenv
from datetime import date, timedelta
import random

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],  # Vite's default port
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Configure Database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///health_app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)

# User Routes
@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        schema = UserSchema()
        data = schema.load(request.json)
        
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            "message": "User created successfully",
            "user_id": new_user.id
        }), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        schema = UserSchema()
        return jsonify(schema.dump(user))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        schema = UserSchema(partial=True)
        data = schema.load(request.json)
        
        for key, value in data.items():
            setattr(user, key, value)
        
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Pain History Routes
@app.route('/api/users/<int:user_id>/pain-history', methods=['POST'])
def add_pain_history(user_id):
    try:
        user = User.query.get_or_404(user_id)
        schema = PainHistorySchema()
        data = schema.load(request.json)
        
        new_pain_record = PainHistory(user_id=user_id, **data)
        db.session.add(new_pain_record)
        db.session.commit()
        
        return jsonify({"message": "Pain history recorded successfully"}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/pain-history', methods=['GET'])
def get_pain_history(user_id):
    try:
        User.query.get_or_404(user_id)  # Verify user exists
        pain_records = PainHistory.query.filter_by(user_id=user_id).all()
        schema = PainHistorySchema(many=True)
        return jsonify(schema.dump(pain_records))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Mood History Routes
@app.route('/api/users/<int:user_id>/mood-history', methods=['POST'])
def add_mood_history(user_id):
    try:
        user = User.query.get_or_404(user_id)
        schema = MoodHistorySchema()
        data = schema.load(request.json)
        
        new_mood_record = MoodHistory(user_id=user_id, **data)
        db.session.add(new_mood_record)
        db.session.commit()
        
        return jsonify({"message": "Mood history recorded successfully"}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/mood-history', methods=['GET'])
def get_mood_history(user_id):
    try:
        User.query.get_or_404(user_id)
        mood_records = MoodHistory.query.filter_by(user_id=user_id).all()
        schema = MoodHistorySchema(many=True)
        return jsonify(schema.dump(mood_records))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Recipe Routes
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    try:
        recipes = Recipe.query.all()
        schema = RecipeSchema(many=True)
        return jsonify(schema.dump(recipes))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        schema = RecipeSchema()
        return jsonify(schema.dump(recipe))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/users/<int:user_id>/meal-plan', methods=['POST'])
def generate_meal_plan(user_id):
    try:
        user = User.query.get_or_404(user_id)
        
        # Delete existing meal plan for the user if it exists
        MealPlan.query.filter_by(user_id=user_id).delete()
        
        # Get all recipes grouped by type
        breakfast_recipes = Recipe.query.filter_by(type='breakfast').all()
        lunch_recipes = Recipe.query.filter_by(type='lunch').all()
        dinner_recipes = Recipe.query.filter_by(type='dinner').all()
        snack_recipes = Recipe.query.filter_by(type='snack').all()
        
        # Get start of current week (Monday)
        today = date.today()
        monday = today - timedelta(days=today.weekday())
        
        # Generate meal plan for each day of the week
        meal_plans = []
        for day in range(7):
            # Randomly select recipes for each meal
            breakfast = random.choice(breakfast_recipes) if breakfast_recipes else None
            lunch = random.choice(lunch_recipes) if lunch_recipes else None
            dinner = random.choice(dinner_recipes) if dinner_recipes else None
            snack = random.choice(snack_recipes) if snack_recipes else None
            # Create meal plan for the day
            meal_plan = MealPlan(
                user_id=user_id,
                week_start_date=monday,
                breakfast_id=breakfast.id if breakfast else None,
                lunch_id=lunch.id if lunch else None,
                dinner_id=dinner.id if dinner else None,
                snack_id=snack.id if snack else None,
                day_of_week=day
            )
            meal_plans.append(meal_plan)
            
        # Save all meal plans
        db.session.add_all(meal_plans)
        db.session.commit()
        
        # Return the generated meal plan
        schema = MealPlanSchema(many=True)
        return jsonify({
            "message": "Meal plan generated successfully",
            "meal_plan": schema.dump(meal_plans)
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/meal-plan', methods=['GET'])
def get_meal_plan(user_id):
    try:
        User.query.get_or_404(user_id)
        meal_plans = MealPlan.query.filter_by(user_id=user_id).order_by(MealPlan.day_of_week).all()
        schema = MealPlanSchema(many=True)
        return jsonify(schema.dump(meal_plans))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add to app.py

from collections import defaultdict

@app.route('/api/users/<int:user_id>/shopping-list', methods=['GET'])
def generate_shopping_list(user_id):
    try:
        # Get user's meal plan
        meal_plans = MealPlan.query.filter_by(user_id=user_id).all()
        
        if not meal_plans:
            return jsonify({"message": "No meal plan found"}), 404
            
        shopping_list = defaultdict(lambda: {
            "quantity": 0,
            "unit": "",
            "details": set()
        })
        
        # Collect ingredients from all recipes in the meal plan
        for plan in meal_plans:
            recipes = [plan.breakfast, plan.lunch, plan.dinner]
            for recipe in recipes:
                if recipe:
                    ingredients = recipe.get_ingredients()  # Use the new helper method
                    for ingredient in ingredients:
                        item = ingredient['item']
                        current = shopping_list[item]
                        
                        # Add quantity if present
                        if ingredient.get('quantity'):
                            if current['unit'] and current['unit'] != ingredient['unit']:
                                # If units don't match, keep them separate
                                item_key = f"{item} ({ingredient['unit']})"
                                shopping_list[item_key]['quantity'] = ingredient['quantity']
                                shopping_list[item_key]['unit'] = ingredient['unit']
                            else:
                                current['quantity'] += ingredient['quantity']
                                current['unit'] = ingredient['unit']
                        
                        # Add details if present
                        if ingredient.get('details'):
                            current['details'].add(ingredient['details'])
        
        # Convert shopping list to final format
        final_list = [
            {
                "item": item,
                "quantity": details['quantity'],
                "unit": details['unit'],
                "details": ', '.join(details['details']) if details['details'] else ""
            }
            for item, details in shopping_list.items()
        ]
        
        # Sort by item name
        final_list.sort(key=lambda x: x['item'])
        
        return jsonify({
            "shopping_list": final_list
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/meal-plan/invalidate-recipe', methods=['POST'])
def invalidate_meal_plan_recipe(user_id):
    try:    
        return jsonify({"message": "Nous allons supprimer le repas de la planification"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')