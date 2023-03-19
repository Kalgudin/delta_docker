import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delta_web.settings')

app = Celery('delta_web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.timezone = 'Europe/Moscow'
# запускаем регулярную задачу
app.conf.beat_schedule = {
    "update_goods": {
        "task": "delta.tasks.regular_update_products",
        "schedule": crontab(minute=0, hour=3),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

