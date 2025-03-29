import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("Diploma")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(['tasks.periodic_tasks'])
