from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Message, Comment
from .serializers import MessageSerializer, CommentSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'update':
            kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs['pk'], user=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.action == 'update':
            kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(Comment, pk=self.kwargs['pk'], user=self.request.user)
