# Models

## Migrations

1. `python manage.py makemigrations`: To create migrations
2. `python manage.py migrate`: To apply migrations
3. `python manage.py showmigrations`: To check migrations history
4. Making migrations to specific app
    * `python manage.py makemigrations your_app_name`
    * `python manage.py migrate your_app_name`

**Common Issues and Fixes**
1. Forgot to apply migrations? → Run `migrate`
2. Database locked or error? → Try `python manage.py migrate --fake`
3. Changed a field type and got errors? → Use `--fake-initial`

## Can We Access One App's Models in Another App in Django?

Yes! In Django, you can access models from one app in another app using import statements and Django’s ORM (Object-Relational Mapping).

🔹 1️⃣ Importing Models from Another App
Each app in Django is a modular Python package, so you can import models from one app into another using:

python
Copy
Edit
from app_name.models import ModelName
Example: Accessing Blog Model from blog App in comments App
📌 Directory Structure
bash
Copy
Edit
my_project/
│── blog/
│   ├── models.py  # Contains Blog model
│── comments/
│   ├── models.py  # Needs to access Blog model
📌 blog/models.py
python
Copy
Edit
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
📌 comments/models.py (Import Blog Model from blog App)
python
Copy
Edit
from django.db import models
from blog.models import Blog  # ✅ Importing Blog model

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)  # ✅ ForeignKey to Blog
    text = models.TextField()
✅ Now, Comment model references Blog using a ForeignKey relationship.

🔹 2️⃣ Cross-App Model Queries
Once models are linked, you can perform queries across apps.

python
Copy
Edit
from comments.models import Comment

# Get all comments for a blog post
blog_post = Blog.objects.get(id=1)
comments = Comment.objects.filter(blog=blog_post)
🔹 3️⃣ Using Related Name for Reverse Queries
You can also query the related model:

python
Copy
Edit
blog_post.comments.all()  # Get all comments for a blog post
(Works because Django automatically creates a reverse relation using related_name.)

🔹 4️⃣ Accessing Models in Views of Another App
You can import models into views.py of a different app:

```python
from blog.models import Blog

def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog_list.html", {"blogs": blogs})
```

🔹 5️⃣ What If Models Are in a Third-Party App?
If you're using a third-party Django package, import the models the same way:

python
Copy
Edit
from third_party_app.models import ThirdPartyModel

##  Foreign Key and Foreign Object in Django Models



