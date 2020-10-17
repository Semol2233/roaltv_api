from rest_framework import serializers
from roaltv_app.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest


# class youtubevideos_playlistseri(serializers.ModelSerializer):

#     class Meta:
#         model = youtube_videoplaylist
#         fields = [
#             'id',
#             'playlist_name',
#             'playlist_code',
#             'channel_id'
#         ]



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
    videos = serializers.SerializerMethodField("get_videos")
    class Meta:
        model = youtube_videoplaylist_atn
        fields = [
            'playlist_name',
            'channel_id',
            'playlist_code',
            'videos'
        ]
    def get_videos(self, obj):
        return "Videos"
    


class shortplssaylist(serializers.ModelSerializer):
    name = serializers.SerializerMethodField("get_name")
    class Meta:
        model = liveweblisttvlist
        fields = [
            'channel_logo',
            'web_link',
            'name'
        ]

    def get_name(self, obj):
        return "News"
    


class atn_about_seri(serializers.ModelSerializer):
    img = serializers.SerializerMethodField("get_img")
    class Meta:
        model = about_atn
        fields = [
            'description',
            'img'
        ]

    def get_img(self, obj):
        return "https://scontent-mxp1-1.xx.fbcdn.net/v/t31.0-8/13415525_1003408123070010_6884761071434198727_o.jpg?_nc_cat=102&_nc_sid=09cbfe&_nc_ohc=-vNgLwex8fIAX_BnbG4&_nc_ht=scontent-mxp1-1.xx&oh=36c34974fd2b8cfb4c741ddfd3b37a93&oe=5FAFDD46"
    

class adcode(serializers.ModelSerializer):

    class Meta:
        model = admove_ad_code
        fields = [
            'ads_page',
            'Ads_SDK_id',
            'ads_code'
        ]