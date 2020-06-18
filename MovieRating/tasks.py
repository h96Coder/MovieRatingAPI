from celery.task import task
from . import email_service

@task
def send_notifiction():
     email_service.send_emails()