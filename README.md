# Fitness Platform Project

This is a *fitness platform* built with **Django (Python)** and **PostgreSQL** for the backend, with a React frontend using only the necessary parts.
The main goal of this project is to develop a backend connected to a basic React frontend.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Environment Variables](#environment-variables)
- [Installation](#installation)

## Description

This project aims to provide a fitness platform with functionalities for creating and sharing exercises, routines, and meals.
It will include backend APIs built with *Django REST Framework* and a functional frontend developed with *React*.

## Features
- CRUD operations for exercises, routines and meals
- Basic user authentication
- Responsive frontend layout
- REST API for the frontend and authorized clients

## Tech Stack

 **Backend:**
 - Python
 - Django
 - Django REST Framework
 - PostgreSQL (hosted on Neon)

 **Frontend:**
 - React
 - Bootstrap

 **DevOps / Tools:**
 - Git
 - Docker
 - AWS (for deployment)

## Requirements

- Dependencies are listed in `requirements.txt`

## Environment Variables

Create a `.env` file in your project root and add:
 - SECRET_KEY=your_secret_key
 - DEBUG=True
 - DATABASE_URL=postgres://user:password@localhost:5432/fitness_db
 - ALLOWED_HOSTS=localhost,127.0.0.1

## Installation

1. Clone the repository:
    git clone https://github.com/pablopalmagarcia/fitness-platform.git
    cd fitness-platform
2. Create and activate a virtual environment:
    python -m venv .venv
    source .venv/bin/activate
3. Install dependencies:
    pip install -r requirements.txt
4. Run database migrations:
    python manage.py migrate
5. Start the development server:
    python manage.py runserver