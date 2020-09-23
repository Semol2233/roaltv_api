from rest_framework import serializers
from roaltv_app.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class cat_list(serializers.ModelSerializer):

    class Meta:
        model = catgory_list
        fields = [
            'id',
            'cat_name'
    ]

class UserDettails(serializers.HyperlinkedModelSerializer):
    catgory         = cat_list(read_only=True,many=True, required=False)
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
    catgory         = cat_list(read_only=True,many=True, required=False)
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

    
class youtubevideos_playlistseri(serializers.ModelSerializer):

    class Meta:
        model = youtube_videoplaylist
        fields = [
            'id',
            'playlist_name',
            'playlist_code'
        ]


class coverpage_seri(serializers.ModelSerializer):

    class Meta:
        model = movie_pageCover
        fields = [
            'moviePgaecover'
        ]


class livetv_pageLink(serializers.ModelSerializer):

    class Meta:
        model = livetvlink
        fields = [
            'livetv_link'
        ]