from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView

from .pagenation import PaginationHandlerMixin
from .api.api import *

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class API_objects(generics.ListAPIView):
    queryset               = post_models.objects.all().order_by('-id')
    serializer_class       = UserDettails
    pagination_class       = StandardResultsSetPagination

# class API_osbjects(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostCreate.objects.all().order_by('?')
#     parser_classes = (MultiPartParser,FormParser,JSONParser)
#     serializer_class       = DRFPostSdderializer
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['channel__id','channel__channelname','title','photo','contentowners__authorsname']
#     lookup_field           = ('slug')


class home_pagedata(generics.ListAPIView):
    queryset               = post_models.objects.all()[:2]
    serializer_class       = UserDettails




class bareking_news(generics.ListAPIView):
    queryset               = post_models.objects.all()[:4]
    serializer_class       = UserDettails


class all_news(generics.ListAPIView):
    queryset               = post_models.objects.all().order_by('-id')
    serializer_class       = UserDettails
    pagination_class       = StandardResultsSetPagination











class dtls_view(generics.RetrieveAPIView):
    queryset           = post_models.objects.all()
    serializer_class   = dtls_sero
    lookup_field       = ('id')


class youtube_playlist(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class youtubevideos_playlist(generics.ListAPIView):
    queryset = youtube_videoplaylist.objects.all().order_by('-id')
    serializer_class = youtubevideos_playlistseri
    pagination_class = youtube_playlist
    
class short_playlist(generics.ListAPIView):
    queryset = youtube_videoplaylist.objects.all()[:1]
    serializer_class = shortplaylist
    pagination_class = youtube_playlist


class API_objedfcts(APIView, PaginationHandlerMixin):
    pagination_class = youtube_playlist

    def get(self, request, category, *args, **kwargs):
        authors = catgory_list.objects.filter(cat_name=category).values('cat_name')
        if authors:
            posts = post_models.objects.filter(catgory__cat_name=category).values('id','title', 'description', 'release_date','img_link').order_by('-id')
            for author in list(authors):
                response = {
                'Sports_page': author['cat_name'],

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)




class coverimg(generics.ListAPIView):
    queryset = movie_pageCover.objects.all().order_by('-id')[:4]
    serializer_class = coverpage_seri
  
    

class livetv_link(generics.ListAPIView):
    queryset = livetvlink.objects.all()
    serializer_class = livetv_pageLink
  


    

class about(generics.ListAPIView):
    queryset = about.objects.all()
    serializer_class = about_seri
  
   
class ad_code(generics.ListAPIView):
    queryset = admove_ad_code.objects.all()
    serializer_class = about_seri
  