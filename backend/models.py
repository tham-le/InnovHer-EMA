# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, validate

db = SQLAlchemy()

class TimestampMixin:
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

# Association Tables
user_favorite_recipes = db.Table('user_favorite_recipes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('created_at', db.DateTime, default=datetime.utcnow)
)

class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Personal Information
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    
    # Health Information
    height = db.Column(db.Float)  # in cm
    weight = db.Column(db.Float)  # in kg
    condition = db.Column(db.String(100))  # primary health condition
    diagnosed = db.Column(db.Boolean, default=False)
    allergies = db.Column(db.Text)
    medications = db.Column(db.Text)
    
    # Relationships
    pain_records = db.relationship('PainHistory', backref='user', lazy=True)
    mood_records = db.relationship('MoodHistory', backref='user', lazy=True)
    favorite_recipes = db.relationship('Recipe', 
                                     secondary='user_favorite_recipes',
                                     lazy='subquery',
                                     backref=db.backref('favorited_by_users', lazy=True))

class Recipe(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # breakfast, lunch, dinner

class PainHistory(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pain_level = db.Column(db.Integer, nullable=False)  # 1-10
    pain_type = db.Column(db.String(50), nullable=False)  # muscle, joint, nerve
    description = db.Column(db.String(255))

class MoodHistory(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)  # happy, sad, anxious, etc.
    mood_description = db.Column(db.String(255))

# Validation Schemas
class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    email = fields.Email(required=True)
    first_name = fields.Str()
    last_name = fields.Str()
    age = fields.Integer(validate=validate.Range(min=0, max=120))
    gender = fields.Str(validate=validate.OneOf(['male', 'female', 'other']))
    height = fields.Float()
    weight = fields.Float()
    condition = fields.Str()
    diagnosed = fields.Boolean()
    allergies = fields.Str()
    medications = fields.Str()

class RecipeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    instructions = fields.Str(required=True)
    image_url = fields.Str(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(['breakfast', 'lunch', 'dinner']))

class PainHistorySchema(Schema):
    pain_level = fields.Int(required=True, validate=validate.Range(min=1, max=10))
    pain_type = fields.Str(required=True, validate=validate.OneOf(['muscle', 'joint', 'nerve']))
    description = fields.Str()

class MoodHistorySchema(Schema):
    mood = fields.Str(required=True)
    mood_description = fields.Str()