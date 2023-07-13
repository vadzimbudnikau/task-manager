## Task Manager - Django-based ToDo Manager

This is a simple ToDo manager implemented using the Django web framework. The web interface is built using the Semantic UI framework (https://semantic-ui.com/).

## Project Setup
Create a new project directory and navigate to it:
    mkdir ToDoDjango && cd ToDoDjango

Set up and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

Initialize a new Git repository:
    git init

Install the required modules:
    pip install django gunicorn

Create a Django project named todoapp and navigate to it:
    django-admin startproject todoapp && cd todoapp

Create a new application named todolist:
    python manage.py startapp todolist

Register the todolist application in the settings.py file:
    INSTALLED_APPS = [
    ...,
    'todolist',
]

Specify the localization and time zone in the settings.py file:
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = '...'

Add the templates directory to the settings.py file:
    TEMPLATES = [
    {
        ...,
        'DIRS': ['templates'],
    },
]

Create the necessary directory structure:
    mkdir templates
    mkdir todolist/static/css
    echo .> .gitignore
    echo .> templates/layout.html
    echo .> templates/index.html
    echo .> todolist/static/todolist/css/style.css
    echo .> README.MD
    echo .> todolist/urls.py

Collect all the static files into the project's static directory:
    python manage.py collectstatic

Create a file containing the project's dependencies:
    pip freeze > requirements.txt

Run the server:
    python manage.py runserver

This will start the server, and you can access the Task Manager application by visiting the provided URL.
