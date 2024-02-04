from celery import Celery
import os


# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skeleton.settings')

app = Celery('skeleton')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routes = {
    'app.tasks.do_task': {
        'queue': 'queue1',
    },
}

app.conf.beat_schedule = {
    'do_task': {
        'task': 'app.tasks.do_task',
        'schedule': 5,
    }
}

app.autodiscover_tasks()

