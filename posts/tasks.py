from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from blog.settings import EMAIL_HOST_USER

User = get_user_model()


@shared_task
def send_messages_about_new_post_task(owner_email: str, message_id: int):
    for user in User.objects.all():
        send_mail(
            'New message',
            f"{owner_email} created a new message with id {message_id}",
            EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
