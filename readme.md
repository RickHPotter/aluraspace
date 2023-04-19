# ABOUT DJANGO

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writitng your app without needing to reinvent the wheel.

It's free and open source, ridiculously fast, reassuringly secure and exceedingly scalable.

Django has its own OMR, uses MVC architecture and has an admin interface.

MVC is the architecture of Django, but it works differently, first of all the name, which is called MTV -> Model, Template, View. Template is the View (V) from MVC, whilst View from MTV is Controller from MVC.

## SETTING UP

After creating a folder for your project, run shell on this folder the following commands ->

`virtualenv venv`
`.venv\Scripts\activate`
`python -m pip install django`

Every time you install something on your virtual environment, remember to run `pip freeze > requirements.txt` to save the dependecies of your project (`pip freeze`) inside a txt file.

### DJANGO ADMIN

To create an admin for Django, we run `django-admin startproject setup .`

To run Django Server, we run `python manage.py runserver`.
