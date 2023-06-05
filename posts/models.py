from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва повідомлення')
    text = models.TextField(verbose_name='Текст повідомлення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст коментаря')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Повідомлення', related_name='comments')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
