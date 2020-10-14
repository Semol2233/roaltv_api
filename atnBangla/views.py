from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView

from roaltv_app.models import *
from atnBangla.api import *




class youtube_playlist(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class atn_youtube_playlist(generics.ListAPIView):
    queryset = youtube_videoplaylist_atn.objects.all().order_by('-id')
    serializer_class = youtubevideos_playlistseri
    pagination_class = youtube_playlist



# class apps_coverimg_view(generics.ListAPIView):
#     queryset = apps_coverimg.objects.all().order_by('-id')
#     serializer_class = apps_coverimg
#     lookup_field       = ('typeimg')


from rest_framework import filters

class apps_coverimgview(generics.ListAPIView):
    queryset           = apps_coverimg.objects.all()
    serializer_class   = coverpage_seriaa
    filter_backends    = [filters.SearchFilter]
    search_fields      = ['typeimg']



class livetvlisst(generics.ListAPIView):
    queryset           = livetvlist.objects.all()
    serializer_class   = livetvlistss
    filter_backends    = [filters.SearchFilter]




class livetvdlts(generics.RetrieveAPIView):
    queryset = livetvlist.objects.all()
    serializer_class = livetvlistss
    lookup_field = ('id')