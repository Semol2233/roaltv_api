from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from roaltv_app.models import *
from atnBangla.api import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import filters






class youtube_playlist(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class atn_youtube_playlist(generics.ListAPIView):
    queryset = youtube_videoplaylist_atn.objects.all().order_by('-id')
    serializer_class = shortplaylist
    pagination_class = youtube_playlist



# class apps_coverimg_view(generics.ListAPIView):
#     queryset = apps_coverimg.objects.all().order_by('-id')
#     serializer_class = apps_coverimg


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




class short_playlist(generics.ListAPIView):
    queryset = youtube_videoplaylist_atn.objects.all()[:1]
    serializer_class = shortplaylist








class polls_detail(generics.ListAPIView):
    queryset = liveweblisttvlist.objects.all()
    serializer_class = shortplssaylist


@api_view()
def fblink(request):
    data = {"data": {
        "fb": "https://www.facebook.com/atnbanglanewsofficial/"


    }}
    return JsonResponse(data)





class livetvhomwlist(generics.ListAPIView):
    queryset = liveweblisttvlist.objects.all()[:2]
    serializer_class = shortplssaylist



@api_view()
def newssite(request):
    data = {"data": {
        "newssite": "https://www.atnbangla.tv",
    }}
    return JsonResponse(data)




class atn_about(generics.ListAPIView):
    queryset = about_atn.objects.all()
    serializer_class = atn_about_seri


class ad_code(generics.ListAPIView):
    queryset = admove_ad_code.objects.all()
    serializer_class = adcode
    filter_backends    = [filters.SearchFilter]
    search_fields      = ['ads_page']






@api_view()
def apps_info(request):
    data = {"data": {
        "data": "ATN Bangla is a Bengali-language digital cable television channel. It transmits from its studio in Dhaka, Bangladesh.This is the first satellite based channel in Bangladesh. The channel is transmitted in South Asia, the Middle East, Europe, and North America",
         "img":"https://i2.wp.com/www.atnbangla.tv/wp-content/uploads/2015/09/chairman-atn-mahfuz.jpg"

    }}
    return JsonResponse(data)


