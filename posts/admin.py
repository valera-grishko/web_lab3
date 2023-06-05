from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Message, Comment


class UserLinkMixin:
    def user_link(self, obj):
        if obj.user is not None:
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:users_customuser_change", args=(obj.user.pk,)),
                obj.user.email
            ))
        return None

    user_link.short_description = 'Користувач'


class MessageLinkMixin:
    def message_link(self, obj):
        if obj.message is not None:
            return mark_safe('<a href="{}">{}</a>'.format(
                reverse("admin:posts_message_change", args=(obj.message.pk,)),
                obj.message.pk
            ))
        return None

    message_link.short_description = 'Повідомлення'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin, UserLinkMixin):
    list_display = ('id', 'name', 'created_at', 'user_link')
    search_fields = ('name', 'user__email')
    icon_name = 'message'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin, UserLinkMixin, MessageLinkMixin):
    list_display = ('id', 'created_at', 'user_link', 'message_link')
    search_fields = ('user__email',)
    icon_name = 'comment'
