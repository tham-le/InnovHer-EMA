# Health API Test Dashboard

A Vue 3 + Vite frontend application for testing a Flask-based Health API, featuring user management, pain tracking, mood tracking, and recipe management.

## Project Structure
```
health-api-test/
├── backend/                  # Flask API
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── diet.py
│   │   ├── health_record.py
│   │   └── user.py
│   ├── requirements.txt
│   └── app.py
│
└── frontend/                # Vue frontend
    ├── src/
    │   ├── components/
    │   │   └── ApiTest.vue
    │   ├── App.vue
    │   └── main.js
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/health-api-test.git
cd health-api-test
```

2. Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Set up environment variables (if needed):
```bash
# Windows
set FLASK_DEBUG=1
set DATABASE_URI=sqlite:///health_app.db

# macOS/Linux
export FLASK_DEBUG=1
export DATABASE_URI=sqlite:///health_app.db
```

5. Run the Flask application:
```bash
python app.py
```

The backend API will be available at `http://localhost:5000`

## Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend application will be available at `http://localhost:5173`

## API Endpoints

### Users
* `POST /api/users` - Create new user
* `GET /api/users/{user_id}` - Retrieve user details
* `PUT /api/users/{user_id}` - Update user information
* `DELETE /api/users/{user_id}` - Delete user

### Pain History
* `POST /api/users/{user_id}/pain-history` - Record new pain entry
* `GET /api/users/{user_id}/pain-history` - Get user's pain history

### Mood History
* `POST /api/users/{user_id}/mood-history` - Record new mood entry
* `GET /api/users/{user_id}/mood-history` - Get user's mood history

### Recipes
* `GET /api/recipes` - List all recipes
* `GET /api/recipes/{recipe_id}` - Get specific recipe details

### Favorite Recipes
* `POST /api/users/{user_id}/favorite-recipes` - Add recipe to favorites
* `GET /api/users/{user_id}/favorite-recipes` - List user's favorite recipes
* `DELETE /api/users/{user_id}/favorite-recipes/{recipe_id}` - Remove recipe from favorites

## Development

### Backend Dependencies
The backend requires the following Python packages:
- Flask
- Flask-CORS
- SQLAlchemy
- Marshmallow

### Frontend Dependencies
The frontend requires:
- Vue 3
- Vuetify 3
- Vite

## Common Issues and Solutions

### CORS Issues
If you encounter CORS errors, make sure:
1. Flask-CORS is properly installed and configured
2. The backend CORS configuration matches your frontend URL

### Database Issues
If you encounter database errors:
1. Make sure the DATABASE_URI environment variable is set correctly
2. Check if the database file has proper permissions
3. Try deleting the database file and letting it recreate on startup

### Network Errors
If you see network errors:
1. Verify both frontend and backend are running
2. Check if the ports (5000 for backend, 5173 for frontend) are available
3. Ensure the backend URL in the frontend matches your Flask server

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details