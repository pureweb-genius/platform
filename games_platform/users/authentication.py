import jwt
from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from .models import CustomUser


class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_heaader = request.headers.get('Authorization')
        if not authorization_heaader:
            return None
        try:
            access_token = authorization_heaader.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        user = CustomUser.objects.filter(id=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')
        return (user, None)

