from rest_framework import authentication
from rest_framework import exceptions
from auth_mine.models import User
from auth_mine.views import SECRET_KEY
import jwt

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            # Extract the token
            token = auth_header.split(' ')[1]
            # Decode the token
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(custom_id=payload['id'])
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except (jwt.InvalidTokenError, User.DoesNotExist, IndexError):
            raise exceptions.AuthenticationFailed('Invalid token') 