from django.db import models
from rest_framework.authtoken.models import Token



def create_api_token(user):#
    ''' Create api token for given user '''
    token = Token.objects.create(user=user)
    return token

