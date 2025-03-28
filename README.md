# Diploma: An E-commerce Project with Django

This project is an e-commerce website built using the Django framework. It aims to provide a platform for animal products, offering a wide range of categories, brands, and promotional offers.

## Table of Contents

- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Structure of env file](#structure-of-env-file)


## Key Features

- User registration and authentication
- Shopping cart functionality
- Product catalog with filtering and sorting options
- Favourite products feature
- Product search functionality
- Promotional offers and discounts

## Getting Started

1. Clone the repository: `git clone https://github.com/Mrslimek/TerritoryZoo.git`
2. Go to project directory: `cd Diploma`
3. Install the required dependencies: `uv sync`
4. Set up the database:
   - Create a new database in your preferred database management system (e.g., PostgreSQL, MySQL, SQLite).
   - Create `.env` file and add necessary data
   - Run the database migrations: `uv run manage.py migrate`
6. Start the development server: `uv run manage.py runserver`

## Structure of env file

Make sure to create an `.env` file in the root directory with the following keys:
- DJANGO_SECRET_KEY
- DJANGO_DEBUG
- DJANGO_ALLOWED_HOSTS
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- GOOGLE_API_KEY (for using google maps)
- YANDEX_API_KEY (for using yandex maps)
- CELERY_BROKER_URL