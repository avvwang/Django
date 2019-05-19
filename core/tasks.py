from celery import Celery
from Django.celery import app

from time import sleep
celery_app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add_test(x,y):
    sleep(10)
    return x+y