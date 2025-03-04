# APIs best practice
how to distinguish between render page or loading page apis and business logic apis in django

## HTML page Load API and Business Logic API


**how to distinguish between render page or loading page apis and business logic apis in django**

In Django, rendering page APIs (used for loading web pages) and business logic APIs (used for backend processing) serve different purposes. You can distinguish between them based on URL structure, views, response types, and app structure.

🔹 `1. Key Differences`
Feature|	Render Page APIs (Page Views)	|Business Logic APIs (Data APIs)
---|---|---
Purpose	|Load and render HTML templates|	Handle backend logic, return JSON/XML
Response Type|	HttpResponse with render()	|JsonResponse, DRF Response, or REST API
View Type|	Function-based views (FBVs) or Class-based views (CBVs)|	API views (Django REST Framework)
Usage|	Used in frontend pages (/home, /dashboard)	|Used in AJAX, mobile apps, external integrations
Data Format|	HTML templates (.html)|	JSON, XML, or raw data
🔹 `2. Organizing in Django`

1️⃣ Render Page APIs (HTML Views)
* Found in the Django app's views.py
* Uses render() to return an HTML page
* Example:
```python
Copy
Edit
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', {"message": "Welcome!"})
```
📌 URLs (urls.py):

```python
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # Render home page
]
```

2️⃣ Business Logic APIs (Data/REST APIs)

* Returns JSON responses
* Used for backend logic, AJAX requests, or external API integrations
* Can be built using Django JsonResponse or Django REST Framework (DRF)

**(A) Using JsonResponse (Basic API)**

```python

from django.http import JsonResponse

def api_get_data(request):
    data = {"status": "success", "message": "API data response"}
    return JsonResponse(data)
```

📌 URLs (urls.py):

```python

urlpatterns += [
    path('api/data/', api_get_data, name='api-data'),  # API endpoint
]
```

(B) Using Django REST Framework (DRF)

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_get_info(request):
    return Response({"message": "This is a business API"})
```

📌 URLs (urls.py):

```python
from django.urls import path
from .views import api_get_info

urlpatterns += [
    path('api/info/', api_get_info, name='api-info'),
]
```
🔹 3. Best Practices
✅ Keep them in separate apps
* web/ → For rendering pages
* api/ → For business logic APIs

Example project structure:

```
myproject/
│── web/  (Render Page APIs)
│   ├── views.py
│   ├── templates/
│   ├── urls.py
│
│── api/  (Business Logic APIs)
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
```

✅ Use Different URL Prefixes
* / → Renders homepage (render(request, "home.html"))
* /dashboard/ → Renders a user dashboard
* /api/ → Business APIs (JsonResponse or DRF)
* /api/user/ → API for user authentication
* /api/device/ → API for IoT device control