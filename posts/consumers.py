from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.decorators import database_sync_to_async
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from djangochannelsrestframework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Message, Comment
from .serializers import MessageSerializer, CommentSerializer

User = get_user_model()


@database_sync_to_async
def user_online(user):
    if isinstance(user, User):
        User.objects.filter(pk=user.pk).update(status=True)


@database_sync_to_async
def user_offline(user):
    if isinstance(user, User):
        User.objects.filter(pk=user.pk).update(status=False)


class UserStatusConsumer:
    async def connect(self):
        await self.accept()
        await user_online(self.scope['user'])

    async def disconnect(self, code):
        await user_offline(self.scope['user'])


class MessageConsumer(
    UserStatusConsumer,
    GenericAsyncAPIConsumer,
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin
):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        return Message.objects.filter(user__email=kwargs.get('email'))

    def get_object(self, **kwargs):
        return get_object_or_404(Message, pk=kwargs['pk'], user=self.scope['user'])


class CommentConsumer(
    UserStatusConsumer,
    GenericAsyncAPIConsumer,
    ListModelMixin,
    CreateModelMixin,
    DeleteModelMixin
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, **kwargs):
        return Comment.objects.filter(message=kwargs.get('message'))

    def get_object(self, **kwargs):
        return get_object_or_404(Comment, pk=kwargs['pk'], user=self.scope['user'])
