import time
from django.conf import settings


def send(x, y):
    time.sleep(20)
    return x + y
