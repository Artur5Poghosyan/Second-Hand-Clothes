Second Hand Clothes API

This repository contains the backend code for the Second Hand Clothes API, built using Django and Django REST Framework (DRF). The project allows users to list, create, update, and delete second-hand clothing items, along with authentication via JWT tokens.

Features

User Authentication: Supports JWT-based authentication.

CRUD Operations: Create, read, update, and delete garments.

API Documentation: Swagger UI and ReDoc integration for API documentation.

Setup Instructions

Follow these steps to set up the project locally:

1. Clone the Repository

git clone <repository_url>
cd second_hand_clothes

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Environment Variables

Create a .env file in the root directory and add the following:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

Replace your_secret_key with a secure key.

5. Apply Migrations

Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate

6. Create a Superuser

python manage.py createsuperuser

7. Run the Server

Start the development server:

python manage.py runserver

Access the Application

API Endpoints: http://127.0.0.1:8000/api/

Admin Panel: http://127.0.0.1:8000/admin/

Swagger Documentation: http://127.0.0.1:8000/api/schema/swagger-ui/

Running Tests

To run tests, execute:

python manage.py test

Project Structure

second_hand_clothes/
    marketplace/         # App containing models, views, and serializers
    second_hand_clothes/ # Project-level settings and URLs
    static/              # Static files
    templates/           # HTML templates (if any)
    manage.py            # Django's CLI utility

API Endpoints

Authentication

Login: /api/token/ (POST)

Refresh Token: /api/token/refresh/ (POST)

Garments

List Garments: /api/clothes/ (GET)

Create Garment: /api/clothes/create/ (POST)

Update Garment: /api/clothes/<id>/update/ (PUT)

Delete Garment: /api/clothes/<id>/delete/ (DELETE)

License

This project is licensed under the MIT License. See the LICENSE file for details.


Contact

For any queries, please reach out to poghosyanarthur00@gmail.com