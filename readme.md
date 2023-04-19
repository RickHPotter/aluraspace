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
