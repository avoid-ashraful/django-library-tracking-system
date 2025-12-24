import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'daily-loan-email': {
        'task': 'library.tasks.check_overdue_loans',
        'schedule': crontab(hour=11, minute=30),
    },
}