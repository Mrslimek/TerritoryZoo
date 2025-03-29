import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("Diploma")

# Указывает на то, где искать конфигурацию celery
app.config_from_object("django.conf:settings", namespace="CELERY")

# Аргумент указывает на то, где нужно искать задачи, помимо стандартных 'tasks.py'
app.autodiscover_tasks(["tasks.periodic_tasks"])
