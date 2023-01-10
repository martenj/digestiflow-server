import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("digestiflow")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

if "production" in os.environ.get("DJANGO_SETTINGS_MODULE"):
    app.conf.task_routes = {
        "*": {"queue": "default"},
    }

    # Explicitely set the name of the default queue to default (is celery).
    app.conf.task_default_queue = "default"

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
