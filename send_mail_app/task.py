from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celery_proj import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all() # send mail to all users
    for user in users:
        mail_subject = "Hi! Celery testing"
        message = "We are testing the celery here!"
        to_email = user.email
        send_mail(
            subject= mail_subject,
            message= message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True, # fail silently without affecting others
        )
    return "Done"