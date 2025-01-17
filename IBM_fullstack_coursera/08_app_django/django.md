# Django
It contains very basics of django

* `$ django-admin startproject mysite djangotutorial` ==> this will create Django project `mysite` inside the folder `djangotutorial`

* `django-admin startproject mysite` ==> This will create `mysite` project inside `mysite` folder
```
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
These files are:

`manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

`mysite/`: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

`mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

`mysite/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

`mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

`mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

`mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.


## Creating App
Your apps can live anywhere in your Python path. In this tutorial, we’ll create our poll app inside the djangotutorial folder.

To create your app, make sure you’re in the same directory as manage.py and type this command:

`$ python manage.py startapp polls`

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```




## Database

Database modifications and additions are done through migrations. The following are used:

```
python3 manage.py makemigrations ==> to create migration file
python3 manage.py migrate ==> to do necessary modifications in the database
```

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your 
`mysite/settings.py` file

### models
models – essentially, your database layout, with additional metadata. The goal is to define your data model in one place and automatically derive things from it.

In **models.py**
```
polls/models.py¶
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

`NOTE: The __str__() method in Python (and Django models) is a special method used to define a human-readable string representation of an object.`

Here, each model (i.e. table) is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
Each field is represented by an instance of a `Field class` – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.

You can use an optional first positional argument to a Field to designate a human-readable name. That’s used in a couple of introspective parts of Django, and it doubles as documentation. If this field isn’t provided, Django will use the machine-readable name. In this example, we’ve only defined a human-readable name for Question.pub_date. For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.

Some Field classes have required arguments. CharField, for example, requires that you give it a max_length. That’s used not only in the database schema, but in validation, as we’ll soon see.

A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

1. Model = Table:
    * Each model corresponds to a single table in the database.
    * Each attribute of the model corresponds to a column in the table.
2. Instances = Rows:
    * Each instance of a model represents a row in the database table.
3. Fields = Columns:
    * Each field in a model corresponds to a column in the database table.


**Process**

1. Change your models (in models.py).

2. Run python manage.py makemigrations to create migrations for those changes

3. Run python manage.py migrate to apply those changes to the database.


## Static Files
Static files are files like `CSS, JavaScript, images, and fonts` that don’t change dynamically and are served to the client as-is. Django `runserver` doesn't deliver them during production, so, it is good to put them in a proper application wise format.

### Folder Structure for Static Files
myproject/
│
├── myapp/
│   ├── static/
│   │   └── myapp/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── script.js
│   │       └── images/
│   │           └── logo.png
│   ├── templates/
│   │   └── base.html
│   └── views.py
│
├── staticfiles/  # Only created during deployment or after `collectstatic` 
├── manage.py
└── settings.py


