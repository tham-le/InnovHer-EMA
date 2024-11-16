from flask import Flask, jsonify, request
from flask_cors import CORS
from models import (
    db, User, Recipe, PainHistory, MoodHistory,
    UserSchema, PainHistorySchema, MoodHistorySchema, RecipeSchema
)
from marshmallow import ValidationError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
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

# Favorite Recipes Routes
@app.route('/api/users/<int:user_id>/favorite-recipes', methods=['POST'])
def add_favorite_recipe(user_id):
    try:
        user = User.query.get_or_404(user_id)
        recipe_id = request.json.get('recipe_id')
        
        if not recipe_id:
            return jsonify({"error": "Recipe ID is required"}), 400
            
        recipe = Recipe.query.get_or_404(recipe_id)
        
        if recipe in user.favorite_recipes:
            return jsonify({"message": "Recipe already in favorites"}), 400
            
        user.favorite_recipes.append(recipe)
        db.session.commit()
        
        return jsonify({"message": "Recipe added to favorites"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/favorite-recipes', methods=['GET'])
def get_favorite_recipes(user_id):
    try:
        user = User.query.get_or_404(user_id)
        schema = RecipeSchema(many=True)
        return jsonify(schema.dump(user.favorite_recipes))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<int:user_id>/favorite-recipes/<int:recipe_id>', methods=['DELETE'])
def remove_favorite_recipe(user_id, recipe_id):
    try:
        user = User.query.get_or_404(user_id)
        recipe = Recipe.query.get_or_404(recipe_id)
        
        if recipe in user.favorite_recipes:
            user.favorite_recipes.remove(recipe)
            db.session.commit()
            return jsonify({"message": "Recipe removed from favorites"})
        else:
            return jsonify({"message": "Recipe not in favorites"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')