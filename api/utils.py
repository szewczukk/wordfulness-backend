from .serializers import *


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': AccountSerializer(user, context={'request': request}).data
    }