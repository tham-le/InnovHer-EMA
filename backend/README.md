# Health Tracking API Documentation

1. Users
   - POST   /api/users                               # Create user
   - GET    /api/users/{user_id}                    # Get user details
   - PUT    /api/users/{user_id}                    # Update user
   - DELETE /api/users/{user_id}                    # Delete user

2. Pain History
   - POST   /api/users/{user_id}/pain-history       # Add pain record
   - GET    /api/users/{user_id}/pain-history       # Get pain history

3. Mood History
   - POST   /api/users/{user_id}/mood-history       # Add mood record
   - GET    /api/users/{user_id}/mood-history       # Get mood history

4. Recipes
   - GET    /api/recipes                            # Get all recipes
   - GET    /api/recipes/{recipe_id}                # Get specific recipe



A Flask-based REST API for managing user health data, including pain and mood tracking, and recipe management.

## Setup
1. Install dependencies (Flask, Flask-CORS, SQLAlchemy, Marshmallow)
2. Set up environment variables:
   - `DATABASE_URI`: Database connection string (default: sqlite:///health_app.db)
   - `FLASK_DEBUG`: Debug mode toggle

## API Endpoints

### Users
- `POST /api/users`
  - Create new user
  - Returns user ID on success

- `GET /api/users/{user_id}`
  - Retrieve user details

- `PUT /api/users/{user_id}`
  - Update user information

- `DELETE /api/users/{user_id}`
  - Delete user

### Pain History
- `POST /api/users/{user_id}/pain-history`
  - Record new pain entry

- `GET /api/users/{user_id}/pain-history`
  - Get user's pain history

### Mood History
- `POST /api/users/{user_id}/mood-history`
  - Record new mood entry

- `GET /api/users/{user_id}/mood-history`
  - Get user's mood history

### Recipes
- `GET /api/recipes`
  - List all recipes

- `GET /api/recipes/{recipe_id}`
  - Get specific recipe details

### Favorite Recipes
- `POST /api/users/{user_id}/favorite-recipes`
  - Add recipe to favorites
  - Required body: `{"recipe_id": number}`

- `GET /api/users/{user_id}/favorite-recipes`
  - List user's favorite recipes

- `DELETE /api/users/{user_id}/favorite-recipes/{recipe_id}`
  - Remove recipe from favorites

## CORS Configuration
- Origin allowed: http://localhost:3000
- Methods allowed: GET, POST, PUT, DELETE
- Headers allowed: Content-Type

## Error Handling
All endpoints return appropriate HTTP status codes:
- 200: Success
- 201: Resource created
- 400: Bad request
- 404: Resource not found
- 500: Server error

Responses include descriptive error messages when appropriate.