# DJANGO

## ABOUT THIS PROJECT

This is a study project done following an [Alura Course](https://cursos.alura.com.br/course/django-templates-boas-praticas).

The instructor is Guilherme Lima.

Most of the `readme.md` is a step-by-step follow-up of what the project is about. There are some referecens here and there about technical stuff that's not extensevily explained or not explained at all. This quotations come from the following sources ->

- [X] Django Documentation [website](https://docs.djangoproject.com/en/4.2/).
- [X] Django for Beginners by **William S. Vincent.**

## ABOUT DJANGO

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writitng your app without needing to reinvent the wheel.

It's free and open source, ridiculously fast, reassuringly secure and exceedingly scalable.

Django has its own OMR, uses MVC architecture and has an admin interface.

MVC is the architecture of Django, but it works differently, first of all the name, which is called MTV -> Model, Template, View. Template is the View (V) from MVC, whilst View from MTV is Controller from MVC.

### MVC STRUCTURE

1. **Model Layer**:
    1. Django provides an abstraction layer (the '*models*') for structuring and manipulating the data of your web application.
    1. A *model* is the single, definitive source of information about your data. It contains the essential fields and behaviours of the data you're storing. Generally, each model maps to a single database table.
        1. Each model is a Python class that subclasses `django.db.models.Model`.
        1. Each attribute of the model represents a database field.
        1. With all of this, Django gives you an automatically-generated database-access API.
2. **View Layer**:
    2. Django has the concept of *views* to encapsulate the logic responsible for processing a user's request and for returning the response.
        2. A *view* (function) is a Python function that takes a web request and returns a web response. This response can be HTML contents of a web page, a redirect, a XML, an HTTP Error, or anything.
        2. The *view* can live anywhere you want, as long as it's on Python path. The convention though, is to put *views* in a file called `views.py` placed in your project or application directory.
3. **Template Layer**:
    3. This layer provides a designer-friendly syntax for rendering the information to be presented to the user.
        3. *Templates* are the way for Django to generate HTML dynamically in a convenient way. A *template* contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.
        3. A Django *template* is a text document or a Python string marked-up. Some constructs are recognised and interpreted by the *template engine*. The main ones are variables and tags.
        3. A *template* is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.

## SETTING UP

After creating a folder for your project, run shell on this folder the following commands ->

`virtualenv venv`
`.venv\Scripts\activate`
`python -m pip install django`

Every time you install something on your virtual environment, remember to run `pip freeze > requirements.txt` to save the dependecies of your project (`pip freeze`) inside a txt file.

### DJANGO ADMIN

To create an admin for Django, we run `django-admin startproject setup .`

To run Django Server, we run `python manage.py runserver`.

To get rid of the warnings, we run `python manage.py migrate` and redo last step.

To create an app (components of a project), we run `python manage.py startapp <app_name>`.

#### CREATING AN APP

Inside the folder created after running the `startapp` command, go to views and add a function that returns an html HttpResponse.

``` python
# gallery/views.py

from django.http import HttpResponse

def fun(request):
    return HttpResponse(<h1>This is an HTML request.</h1>)
```

After that, we have to import that template to a url endpoint inside setup/urls.py, adding our function to a new path we'll create in this pyfile.

``` python
# setup/urls.py

from gallery.views import fun

urlpatterns = [
    # ...
    path('', fun)
]
```

But as time goes by 'setup.py' will be flooded with paths, so instead of doind it this way we could set a 'url.py' to every app folder we create, and then importing all its views to this file, and only this file to 'setup/urls.py'.

``` python
# gallery/urls.py

from django.urls import path
from gallery.views import fun

urlpatterns = [
    # ...
    path('', fun)
]
```

``` python
# setup/urls.py

from django.urls import path, include

urlpatterns = [
    # ...
    path('', include('gallery.urls')),
]
```

#### ADDING TEMPLATES

In views.py, what we expect to return is not a raw html string, but a file. To do so, we have to set first a dir to our templates files.

- Create a folder templates at the root of the project.
- Access `setup/settings.py` and add the following code ->

``` python
# setup/settings.py

# ...
TEMPLATES = [
    {
        # ...
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ]
        # ...
    }
]
# ...
```

- Add an html file inside templates. Let's call it `index.html`.
- Use the `render` function of `django.shortcuts` to return that html file.

``` python
# gallery.views.py

from django.shortcuts import render

def fun(request):
    return render(request, 'index.html')
```

- Inside `setup/static` folder, feed it with styles and assets, and edit `setup/settings.py` to accept them as static files of this project.

```python
# setup/settings.py

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- Run `python manage.py collectstatic` to make Django recognise all the static files you fed your project with.
- Now it's time to load the static files.

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en-GB">
    
<head>
    <!-- ... -->
    <title>Alura Space</title>
    {% load static %}
    <link rel="stylesheet" href="{% static '/styles/style.css' %}">
    <!-- ... -->
</head>
<!-- ... -->
```

For every static file you load by first inserting the line `{% load static %}`, then for every *href* and *src*, you input its content inside `{% static 'path_to_asset' %}`.

#### URL NAME

#### PARTIALS
