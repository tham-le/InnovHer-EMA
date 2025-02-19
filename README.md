# EMA: Personalized Health Management for Rheumatism

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

EMA (named after the mother of the creator, Andrea) is a comprehensive health management application designed to assist individuals suffering from rheumatic conditions.  It provides personalized daily tracking, dietary planning, activity recommendations, and symptom analysis, leveraging a scientifically-backed approach to improve quality of life. The application combines a Flask-based RESTful backend (Python) with a modern, responsive Vue 3 frontend (JavaScript/TypeScript).

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
  - [Backend (Flask API)](#backend-flask-api)
  - [Frontend (Vue 3)](#frontend-vue-3)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Database Seeding](#database-seeding)
- [Development](#development)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Contributing](#contributing)
- [License](#license)
- [Common Issues and Solutions](#common-issues-and-solutions)


## Project Overview

EMA's core functionality revolves around helping users manage their rheumatic condition by:

*   **Tracking Pain & Mood:** Users can record their daily pain levels, pain types (articular, muscular, inflammatory, stiffness, fatigue, swelling), and mood, along with detailed notes.
*   **Personalized Meal Planning:**  The application generates weekly meal plans tailored to the user's profile, featuring anti-inflammatory recipes (focused on the Mediterranean diet) with ingredients like fatty fish, whole grains, legumes, nuts, seeds, olive oil, and fresh fruits/vegetables.  The meal plans include breakfast, lunch, and dinner options.
*   **Shopping List Generation:**  EMA automatically creates a shopping list based on the user's weekly meal plan, consolidating ingredients and quantities.  The shopping list includes a feature to mark items as purchased (with persistence using `localStorage`).
*   **Activity Logging:** Users can track their physical activities, with examples provided (running, yoga, swimming, strength training, stationary biking). YouTube video links are included for some activities.
*   **Microbiote Information:** A dedicated page provides information about the human intestinal microbiome, including its composition, functions, and impact on health.
*   **Detailed Pathology Tracking:** A "Pathologie" page allows users to log their daily pain levels, select pain types, and add detailed notes.  The app displays a history chart of pain levels.
*   **User Profile Management:** Users can manage their personal information (username, email, first name, last name, age, gender) and health information (height, weight, primary health condition, diagnosis status, allergies, medications).
* **Recipe invalidation**: A user can click on a button to invalidate a recipe and give a reason.

## Features

*   **User Authentication:** (Currently, user ID 1 is hardcoded for demonstration purposes.  Full authentication is not yet implemented.)
*   **Pain & Mood Tracking:** Daily recording of pain level, type, and description; mood recording with description.
*   **Meal Planning:**
    *   Weekly meal plan generation with breakfast, lunch, and dinner.
    *   Recipes based on an anti-inflammatory diet.
    *   Recipe details view (ingredients, instructions).
    *   Ability to switch between daily and weekly views.
    *  Shopping list feature.
    * Recipe Invalidity.
*   **Activity Tracking:** Log of physical activities.
*   **Responsive Design:**  Optimized for mobile, tablet, and desktop viewing.
*   **Interactive UI:**  Uses Vuetify 3 for a modern and engaging user experience.
*   **Data Visualization:**  Charts.js (via vue-chartjs) for pain history visualization.

## Directory Structure

```
tham-le-innovher-ema/
├── README.md                   <- This file
├── package.json                <- Node.js package file (for frontend dependencies)
├── backend/
│   ├── README.md               <- Backend API documentation
│   ├── app.py                  <- Flask application (main API logic)
│   ├── models.py               <- Database models (SQLAlchemy)
│   ├── requirements.txt        <- Python dependencies
│   └── seed-script.py          <- Script to populate the database with initial data
└── frontend/
    ├── index.html              <- Main HTML file
    ├── package-lock.json       <- Detailed npm dependency tree
    ├── package.json            <- Frontend dependencies and scripts
    ├── vite.config.js          <- Vite configuration
    └── src/
        ├── App.vue             <- Main Vue application component
        ├── main.js             <- Vue application entry point
        ├── assets/
        │   └── images/         <- Images for recipes, etc.
        ├── components/
        │   ├── ApiTest.vue           <- (Outdated) API testing component
        │   ├── CircleProgress.vue  <- Reusable circular progress bar component
        │   ├── NavigationFooter.vue<- Navigation footer component
        │   └── NavigationHeader.vue<- Navigation header component
        ├── composables/
        │   ├── useResponsive.js    <- Reusable responsive logic (isMobile, isTablet, isDesktop)
        │   └── useScreen.js         <- Screen dimension utility.
        ├── page/
        │   ├── AboutUs.vue       <- "About Us" page
        │   ├── Acti.vue          <- Activity tracking page
        │   ├── Aliment.vue       <- Meal planning and recipe page
        │   ├── Landing.vue       <- Landing page with navigation circles
        │   ├── Microbiote.vue    <- Microbiome information page
        │   ├── Patho.vue         <- Pain tracking page
        │   ├── Profile.vue       <- User profile management page
        │   ├── acti.css          <- (Unused) CSS for the Acti.vue page
        │   └── index.css         <- (Unused) Generic CSS file
        ├── plugins/
        │   ├── vuetify.js        <- Vuetify configuration
        │   └── webfontloader.js  <- (Unused) Web font loader
        └── router/
            └── index.js          <- Vue Router configuration
```

## Prerequisites

*   **Python 3.8+** (with `pip`)
*   **Node.js 16+** (with `npm`)

## Setup & Installation

### Backend (Flask API)

1.  **Clone the Repository:**

    ```bash
    git clone git@github.com:tham-le/InnovHer-EMA.git
    cd tham-le-innovher-ema/backend
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4. **Load .env file**
    ```bash
    pip install python-dotenv
    ```

5.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

    The API will be accessible at `http://localhost:5000`.

### Frontend (Vue 3)

1.  **Navigate to the Frontend Directory:**

    ```bash
    cd ../frontend  # From the backend directory
    ```

2.  **Install Dependencies:**

    ```bash
    npm install
    ```

3.  **Run the Development Server:**

    ```bash
    npm run dev
    ```

    The frontend application will be accessible at `http://localhost:5173` (or a different port if 5173 is in use). Vite will automatically hot-reload changes.

## API Endpoints

All API endpoints are prefixed with `/api`.

| Method | Endpoint                               | Description                                     |
| :----- | :------------------------------------- | :---------------------------------------------- |
| `POST` | `/users`                               | Create a new user.                              |
| `GET`  | `/users/<int:user_id>`                 | Get user details.                               |
| `PUT`  | `/users/<int:user_id>`                 | Update user information.                        |
| `DELETE` | `/users/<int:user_id>`                 | Delete a user.                                  |
| `POST` | `/users/<int:user_id>/pain-history`    | Add a pain history record.                      |
| `GET`  | `/users/<int:user_id>/pain-history`    | Get pain history for a user.                    |
| `POST` | `/users/<int:user_id>/mood-history`    | Add a mood history record.                      |
| `GET`  | `/users/<int:user_id>/mood-history`    | Get mood history for a user.                    |
| `GET`  | `/recipes`                             | Get all recipes.                                |
| `GET`  | `/recipes/<int:recipe_id>`              | Get a specific recipe.                          |
| `POST` | `/users/<int:user_id>/meal-plan`       | Generate a meal plan for the user.            |
| `GET`  | `/users/<int:user_id>/meal-plan`       | Get the user's current meal plan.             |
| `GET`  | `/users/<int:user_id>/shopping-list`   | Generate a shopping list for the user's meal plan.|
|`POST`| `/users/<int:user_id>/meal-plan/invalidate-recipe` | Invalidate meal plan recipe |

## Environment Variables
- `DATABASE_URI`: The database connection string (default: `sqlite:///health_app.db`).
- `FLASK_DEBUG`:  Enable Flask's debug mode (set to `1` for development, `0` for production).

## Database Seeding

The `backend/seed-script.py` file provides a convenient way to populate the database with initial data (sample users, recipes, pain history, and mood history).  To seed the database:

1.  **Make sure you are in the `backend` directory.**
2.  **Make sure your virtual environment is activated.**
3.  **Run the script:**

    ```bash
    python seed-script.py
    ```

    This will drop all existing tables and recreate them with the sample data.

## Development

### Backend

*   **Flask:**  The core web framework.
*   **Flask-CORS:**  Handles Cross-Origin Resource Sharing, allowing the frontend to make requests to the backend.
*   **SQLAlchemy:**  Object-Relational Mapper (ORM) for interacting with the database.
*   **Marshmallow:**  Used for object serialization/deserialization and validation.
* **python-dotenv:** Used to load env file.

### Frontend

*   **Vue 3:**  JavaScript framework for building user interfaces.
*   **Vuetify 3:**  Material Design component framework for Vue.
*   **Vite:**  Fast build tool and development server.
*   **Vue Router:**  Official router for Vue.js.
*   **Chart.js & vue-chartjs:**  For creating charts (pain history).
*   **date-fns:**  For date manipulation and formatting.

## Contributing

1.  **Fork the repository.**
2.  **Create a new branch:** `git checkout -b feature/your-feature-name`
3.  **Make your changes and commit them:** `git commit -m "Add some feature"`
4.  **Push to the branch:** `git push origin feature/your-feature-name`
5.  **Create a pull request.**

## License

This project is licensed under the MIT License.  See the `LICENSE` file (not provided in the original files, but implied) for details.

## Common Issues and Solutions

*   **CORS Errors:** Ensure Flask-CORS is correctly configured in `backend/app.py` to allow requests from the frontend origin (`http://localhost:5173` by default).  The current setup allows all origins (`"origins": "*"`) for development.  In a production environment, restrict this to your specific frontend domain.

*   **Database Errors:** Verify that the `DATABASE_URI` environment variable is set correctly.  If using SQLite (the default), ensure the database file (`health_app.db` by default) has appropriate permissions.

*   **Network Errors:** Confirm that both the backend (Flask) and frontend (Vite) servers are running and accessible on their respective ports (5000 and 5173 by default).  Check for any firewall rules that might be blocking communication.

*   **Missing Images:** The frontend code assumes that recipe images are located in `frontend/src/assets/images/`.  Make sure that you place the necessary image files (e.g., `salmon.jpg`, `breakfast.jpg`, etc.) in that directory, or update the `getImageUrl` function in `frontend/src/page/Aliment.vue` to point to the correct location.  A `default-recipe.jpg` is also referenced as a fallback.

* **Frontend API URL:** The frontend components use `import.meta.env.VITE_API_URL` to get the backend API base URL.  Make sure this environment variable is correctly set to `http://localhost:5000` (or your backend's URL). You can set this in a `.env` file in the `frontend` directory:

   ```
   VITE_API_URL=http://localhost:5000/api
   ```

* **Dependency Conflicts:** If you encounter issues after installing dependencies, try deleting your `node_modules` directory and `package-lock.json` (in the `frontend` directory) and running `npm install` again.  This will rebuild the dependency tree from scratch.

* **Hardcoded User ID:**  The current implementation uses a hardcoded user ID (1) throughout the frontend.  This should be replaced with a proper authentication system in a production environment.

* **Outdated `ApiTest.vue`:** The `ApiTest.vue` component is outdated and not actively used in the application's main flow. It can be safely removed or updated to reflect the current API structure.

* **Unused CSS Files:** The `acti.css` and `index.css` files in the `frontend/src/page/` directory appear to be unused. These can be removed to clean up the project.

* **`webfontloader.js`:** The `webfontloader.js` plugin is present but the font loading configuration seems incomplete, and the Agbalumo font is included in the HTML, making the plugin redundant.

* **Typescript (partial):** The `Acti.vue` contains typescript code. For a better and uniform code, use typescript for all the project, or remove the type definition.
