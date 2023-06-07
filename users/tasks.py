from celery import shared_task
from django.core.mail import send_mail

from blog.settings import EMAIL_HOST_USER


@shared_task
def send_registration_message(email: str):
    send_mail(
        'Registration',
        "You've been registered successfully!",
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
