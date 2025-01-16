# Django deployment
This file deals with the deployment of django application on server and other advanced features.

1. `DEBUG = False`

## Static Files
Django ships with a `lightweight server` called `runserver `that allows us to see live previews of our Django application. It promotes faster development, is great for development purposes, and is used during development not in production. `DEBUG=True` is a way to tell Django that we are currently in the development phase and the runserver can serve the static files. When we set `DEBUG=False`, the Django default server won't work, it requires the `ALLOWED_HOSTS` and some production configuration.

To serve static files in production, we can use `Amazon S3, Azure Blob Storage, Digital Ocean, etc.` However, we can configure a few settings allowing our web server to serve the static files.

### How Static Files Are Handled 
1. When `DEBUG = True` (development mode):
    * Django serves static files directly using the `django.contrib.staticfiles` app.
    * This is convenient for development but not suitable for production due to the reasons mentioned above.

2. When `DEBUG = False`
    * Django does not automatically serve static files.
    * You need to configure your production environment to serve static files using a web server like Nginx, Apache, or a CDN.

### Steps to Serve Static Files in Production
1. Run collectstatic Command
    * Django collects all static files into the directory specified in the STATIC_ROOT setting.
    * `python manage.py collectstatic`
2. Configure `STATIC_ROOT`
    * Set `STATIC_ROOT` to a directory where collected static files will be stored.
    * `STATIC_ROOT = "/path/to/staticfiles/"`
3. Configure a Web Server to Serve Static Files    
    * Use a production-ready web server like Nginx or Apache.

### Image path or other static path in coding
No, you do not need to manually change the image paths or references in your HTML templates after running the collectstatic command in Django. Django's collectstatic command is designed to gather all static files (including images, CSS, JavaScript, etc.) from various app directories and place them into the directory specified by the STATIC_ROOT setting. 

1. Static File Handling in Templates:
    * In Django templates, static files are referenced using the {% static %} template tag.
    * <img src="{% static 'images/logo.png' %}" alt="Logo">
    * The `{% static %}` tag dynamically resolves to the correct path to your static files, whether in development `(DEBUG = True) or production (DEBUG = False)`.
2. STATIC_URL Setting:
    * The `STATIC_URL` setting defines the base URL for serving static files.
    * When `DEBUG = True`, Django serves files from STATICFILES_DIRS.
    * When `DEBUG = False`, the STATIC_URL prefix works with the files collected into STATIC_ROOT.
    * Example in `settings.py`: `STATIC_URL = '/static/'`
    * In production, if the static files are served via `/static/`, the `{% static %}` tag ensures the correct URL is generated, regardless of whether the file resides in the app's static folder or the collected directory.

**Key Points**

1. Ensure all static file references in templates use `{% static %}`.
2. Verify the `STATIC_URL` and `STATIC_ROOT` settings are correctly configured.
3. Make sure you configure your production web server (e.g., `Nginx` or `Apache`) to serve the static files from the `STATIC_ROOT` directory.


## WSGI
WSGI (Web Server Gateway Interface) is a specification that defines how web servers communicate with web applications written in Python. It acts as a standard interface between web servers (such as Apache, Nginx, or Gunicorn) and Python web applications or frameworks (such as Flask, Django, or Pyramid).

The purpose of WSGI is to provide a common interface for Python web applications to interact with any web server, making Python web development more flexible and standardized.

Here’s a brief overview of how WSGI works:

Web Server: The web server receives HTTP requests from clients (browsers).
WSGI Interface: The web server uses WSGI to forward these requests to the Python web application.
Python Web Application: The application processes the request (e.g., by querying a database, rendering a template) and generates an HTTP response.
WSGI Interface: The Python application returns the response via the WSGI interface.
Web Server: The web server sends the response back to the client.
WSGI defines a simple and consistent format for both the input (request) and output (response) that is passed between the server and the application. It makes Python-based web frameworks portable across different web servers.

WSGI stands for Web Server Gateway Interface. It is a specification for a simple and universal interface between web servers and Python web applications or frameworks. WSGI is part of the Python standard (defined in PEP 333 and updated with PEP 3333 for Python 3).

Purpose of WSGI
To provide a standardized way for web servers to communicate with Python applications.
To separate the web server and the web application logic, enabling the development of portable web applications that can run on any WSGI-compliant server.
How WSGI Works
A WSGI server (like Gunicorn, uWSGI, or mod_wsgi) listens for HTTP requests from clients, translates them into a Python-specific format, and sends them to a WSGI-compatible application.
A WSGI application is a callable (usually a function or a class with a __call__ method) that accepts two arguments:
environ: A dictionary containing CGI-like environment variables.
start_response: A callable to start the HTTP response.
The WSGI application processes the request, generates a response, and passes it back to the server, which sends it to the client.

Example WSGI Application
Here's a minimal WSGI application:

python
Copy
Edit
def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello, WSGI World!"]

 To run this, you need a WSGI server like Gunicorn:
 gunicorn myapp:simple_app
Benefits of WSGI
Portability: Any WSGI-compliant application can run on any WSGI-compliant server.
Flexibility: Decouples application logic from server specifics.
Scalability: Enables integration with robust WSGI servers for handling production-level traffic.
Popular WSGI Servers
Gunicorn: A Python WSGI HTTP server often used with Flask, Django, and other frameworks.
uWSGI: A fast application server that supports multiple languages, including Python.
mod_wsgi: An Apache module for hosting WSGI applications.
Relationship with Frameworks
Modern Python web frameworks like Flask, Django, FastAPI, and Pyramid are WSGI-compliant, meaning they can interface with any WSGI server. However, some newer frameworks like FastAPI are moving toward ASGI (Asynchronous Server Gateway Interface) for better support of asynchronous features.









