from __future__ import absolute_import, unicode_literals
import os


from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_proj.settings')

app = Celery('celery_proj')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Manila')

app.config_from_object(settings, namespace='CELERY')

#Celery Beat settings
app.conf.beat_schdeule = {
    
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')