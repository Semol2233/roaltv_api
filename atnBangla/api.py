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


class livetvlistss(serializers.ModelSerializer):

    class Meta:
        model = livetvlist
        fields = [
            'id',
            'channe_name',
            'channel_logo',
            'channel_tvurl',
            'release_date',

        ]



class shortplaylist(serializers.ModelSerializer):

    class Meta:
        model = youtube_videoplaylist_atn
        fields = [
            'playlist_name',
            'channel_id',
            'playlist_code'
        ]


class shortplssaylist(serializers.ModelSerializer):

    class Meta:
        model = liveweblisttvlist
        fields = [
            'channel_logo',
            'web_link',
        ]




class atn_about_seri(serializers.ModelSerializer):

    class Meta:
        model = about_atn
        fields = [
            'description'
        ]


class adcode(serializers.ModelSerializer):

    class Meta:
        model = admove_ad_code
        fields = [
            'ads_page',
            'Ads_SDK_id',
            'ads_code'
        ]