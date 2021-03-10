from celery import shared_task
from .send_mail import send


@shared_task
def send_dingtalk_message(x, y):
    return send(x, y)
