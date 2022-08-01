import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_sheet_data.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()