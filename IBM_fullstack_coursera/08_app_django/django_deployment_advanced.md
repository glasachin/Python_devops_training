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

### Configuration in settings.py

**URL to access static files**

STATIC_URL = '/static/'

**Absolute path where collected static files will be stored (for production)**
STATIC_ROOT = BASE_DIR / 'staticfiles'

**Additional directories to search for static files (optional)**
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # For project-level static files
]



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

### Purpose of WSGI
* To provide a standardized way for web servers to communicate with Python applications.
* To separate the web server and the web application logic, enabling the development of portable web applications that can run on any WSGI-compliant server.
### How WSGI Works
* A WSGI server (`like Gunicorn, uWSGI, or mod_wsgi`) listens for HTTP requests from clients, translates them into a `Python-specific format`, and sends them to a WSGI-compatible application.
* A WSGI application is a callable (usually a function or a class with a __call__ method) that accepts two arguments:
    1. `environ`: A dictionary containing CGI-like environment variables.
    2. `start_response`: A callable to start the HTTP response.
The WSGI application processes the request, generates a response, and passes it back to the server, which sends it to the client.

### Benefits of WSGI
1. Portability: Any WSGI-compliant application can run on any WSGI-compliant server.
2. Flexibility: Decouples application logic from server specifics.
3. Scalability: Enables integration with robust WSGI servers for handling production-level traffic.
### Popular WSGI Servers
1. `Gunicorn`: A Python WSGI HTTP server often used with Flask, Django, and other frameworks.
2. `uWSGI`: A fast application server that supports multiple languages, including Python.
3. `mod_wsgi`: An `Apache module` for hosting WSGI applications.
### Relationship with Frameworks
Modern Python web frameworks like `Flask, Django, FastAPI, and Pyramid are WSGI-compliant`, meaning they can interface with any WSGI server. However, some newer frameworks like FastAPI are moving toward ASGI (Asynchronous Server Gateway Interface) for better support of asynchronous features.

## ASGI
ASGI stands for `Asynchronous Server Gateway Interface`. It is a specification designed to provide a standard interface between asynchronous-capable Python web servers, applications, and frameworks. It was created as an evolution of WSGI to support modern web development requirements, such as handling asynchronous programming and protocols beyond HTTP.

### Purpose of ASGI
* To support asynchronous frameworks and libraries, which are increasingly common in Python.
* To enable handling of long-lived connections, such as WebSockets, HTTP/2, and other real-time communication protocols.
* To build on the foundation of WSGI while extending its capabilities to include both synchronous and asynchronous communication.

ASGI is defined in ASGI specification.

### How ASGI Works
An `ASGI server (e.g., Uvicorn, Daphne, Hypercorn)` interacts with an ASGI application using a standardized protocol. The application is defined as a callable that takes two arguments:

1. `scope`: A dictionary containing details about the connection (e.g., HTTP request, WebSocket connection, or other protocol metadata).
2. `receive`: An asynchronous callable to receive events from the client (e.g., HTTP body data or WebSocket messages).
3. `send`: An asynchronous callable to send events to the client (e.g., HTTP responses or WebSocket messages).


### Features of ASGI
1. `Asynchronous Support`: Allows handling of asynchronous I/O operations, enabling high concurrency.
2. `Protocol Agnostic`: Supports protocols like HTTP, WebSockets, and more.
3. `Backward Compatibility`: Can interoperate with WSGI applications using adapters.
4. `Scalability`: Enables better handling of real-time communication and long-lived connections.

### Popular ASGI Servers
1. `Uvicorn`: A lightning-fast ASGI server built on uvloop and httptools.
2. `Daphne`: Developed as part of the Django Channels project.
3. `Hypercorn`: An ASGI server compatible with HTTP/2 and WebSockets.


## Comparison: ASGI vs. WSGI
Feature	|WSGI|	ASGI
---|---|---
Protocols Supported|	HTTP|	HTTP, WebSockets, HTTP/2
Async Support|	No|	Yes
Long-lived Connections	|Limited	|Fully supported
Use Cases|	Traditional web apps	|Real-time apps, APIs, WebSockets
Modernity|	Older standard (2003)|	Newer standard (2018)


## Questions

**If django creates a thread for one api hit then what will happen when 100 users simultaneously hit the same api**

When 100 users simultaneously hit the same API in a Django application, how the system handles the load depends on the following factors:

1. Django's Default Behavior with Threads
WSGI Server:

Django itself does not handle threading; it delegates that responsibility to the underlying WSGI server (e.g., Gunicorn, uWSGI, or Django's development server).
The default Django development server is single-threaded and not suitable for production. For simultaneous requests, you must use a production-ready WSGI server.
Threading in WSGI Servers:

Many WSGI servers (e.g., Gunicorn) can be configured to use multiple workers and threads.
Each request is handled by a worker process or thread, depending on the server configuration.
2. What Happens When 100 Requests Hit the Same API?
Requests Are Distributed Across Workers:

Each worker or thread processes one request at a time.
If your server has limited workers/threads (e.g., 10 threads), requests exceeding this number will be queued.
Concurrency:

If the WSGI server is configured with multiple threads, it can handle requests concurrently, but it’s limited by the number of available threads.
Queuing:

If the number of incoming requests exceeds the capacity of the threads/workers, the extra requests will be queued.
The queue size is configurable in many WSGI servers. If the queue fills up, additional requests may be dropped or rejected.
Blocking Operations:

If your API performs blocking operations (e.g., database queries, file I/O, external API calls), it can tie up a thread and reduce the server's ability to handle concurrent requests.
This can lead to increased response times or timeouts for users.
3. Key Factors Impacting Performance
Number of Workers/Threads:

More workers/threads can handle more simultaneous requests but require more system resources (CPU, memory).
Request Processing Time:

If the API is computationally intensive or has slow external dependencies, it will reduce throughput.
Database and External Dependencies:

Slow database queries or external API calls can become bottlenecks, limiting how quickly requests can be processed.
Server Hardware:

CPU, memory, and I/O capabilities determine how many requests your server can handle simultaneously.
4. How to Handle High Concurrency
Use an Asynchronous Server (Optional):

Django, by default, is synchronous. Consider using ASGI (Django with an ASGI server like Daphne or Uvicorn) for truly asynchronous handling.
Optimize Worker and Thread Configuration:

Tune your WSGI/ASGI server configuration for your workload.
Example for Gunicorn:
bash
Copy
Edit
gunicorn --workers=4 --threads=8 myproject.wsgi:application
Optimize the API Code:

Avoid blocking operations.
Use asynchronous libraries for database queries or I/O if using ASGI.
Implement Caching:

Use caching (e.g., Redis, Memcached) to reduce the need for repetitive database queries or expensive computations.
Horizontal Scaling:

Add more application servers behind a load balancer to distribute traffic.
Database Optimization:

Index database tables appropriately and optimize queries to reduce latency.
5. Summary
Django's default configuration (development server) is not suitable for handling simultaneous requests in production.
Using a production-grade WSGI server like Gunicorn or uWSGI allows you to handle multiple requests concurrently by configuring multiple workers and threads.
For 100 simultaneous requests:
Requests are queued if workers/threads are busy.
Blocking operations can reduce the number of requests the server can handle concurrently.
For optimal performance:
Use appropriate server configurations, caching, and database optimizations.
Consider using ASGI for highly concurrent and non-blocking APIs.






