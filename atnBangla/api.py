from rest_framework import serializers
from roaltv_app.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest


class youtubevideos_playlistseri(serializers.ModelSerializer):

    class Meta:
        model = youtube_videoplaylist
        fields = [
            'id',
            'playlist_name',
            'playlist_code',
            'channel_id'
        ]



class coverpage_seriaa(serializers.ModelSerializer):

    class Meta:
        model = apps_coverimg
        fields = [
            'moviePgaecover',
            'typeimg'
        ]
