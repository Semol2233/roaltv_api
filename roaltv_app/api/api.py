from rest_framework import serializers
from roaltv_app.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model





class UserDettails(serializers.ModelSerializer):

    class Meta:
        model = post_models
        fields = [
            'id',
            'title',
            'catgory',
            'description',
            'release_date',
            'img_link'
        ]

    

class dtls_sero(serializers.ModelSerializer):

    class Meta:
        model = post_models
        fields = [
            'id',
            'title',
            'catgory',
            'description',
            'release_date',
            'img_link'
        ]

    
