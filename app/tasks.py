from .celery_worker import celery_app
import time

@celery_app.task(bind=True)
def add_five(self):
    time.sleep(5)
    return 5 + 5