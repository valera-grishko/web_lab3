from rest_framework.routers import SimpleRouter

from .viewsets import MessageViewSet, CommentViewSet

router = SimpleRouter()

urlpatterns = [

]

router.register('messages', MessageViewSet, basename='messages')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns += router.urls
