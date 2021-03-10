import time
from celery import Celery

app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1/2')


@app.task
def add(x, y):
    time.sleep(20)
    return x + y
