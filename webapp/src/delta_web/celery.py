import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delta_web.settings')

app = Celery('delta_web')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.timezone = 'Europe/Moscow'
app.conf.beat_schedule = {
    "update_goods": {
        "task": "delta.tasks.regular_update_products",
        "schedule": crontab(minute=0, hour=3),
        "args": ("my args in SETTINGS - ", "minute=0, hour=3",),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('Calls test("hello") every 10 seconds.'), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world - every 30 seconds'), expires=10)
#
#     # Выполнять ежедневно в полночь.
#     sender.add_periodic_task(
#         crontab(minute=0, hour=0),
#         test.s('Happy Mondays!'),
#     )


@app.task
def test(arg):
    print(arg)


