# Django deployment
This file deals with the deployment of django application on server and other advanced features.

1. `DEBUG = False`

## Static Files
Django ships with a `lightweight server` called `runserver `that allows us to see live previews of our Django application. It promotes faster development, is great for development purposes, and is used during development not in production. `DEBUG=True` is a way to tell Django that we are currently in the development phase and the runserver can serve the static files. When we set `DEBUG=False`, the Django default server won't work, it requires the `ALLOWED_HOSTS` and some production configuration.

To serve static files in production, we can use `Amazon S3, Azure Blob Storage, Digital Ocean, etc.` However, we can configure a few settings allowing our web server to serve the static files.



