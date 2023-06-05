import django
import os
import jwt
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.db import close_old_connections
from django.conf import settings
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')


django.setup()

User = get_user_model()


@database_sync_to_async
def get_user(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
    except Exception:
        return AnonymousUser()
    try:
        user = User.objects.get(id=payload['user_id'])
    except User.DoesNotExist:
        return AnonymousUser()
    return user


class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        try:
            jwt_key = [item for item in scope['headers'] if b'authorization' in item][0][1].decode('utf-8').split()[1]
        except ValueError:
            jwt_key = None
        scope['user'] = await get_user(jwt_key)
        return await super().__call__(scope, receive, send)
