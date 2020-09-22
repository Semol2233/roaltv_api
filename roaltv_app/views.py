from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins 
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


from .api.api import *

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
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


class dtls_view(generics.RetrieveAPIView):
    queryset           = post_models.objects.all()
    serializer_class   = dtls_sero
    lookup_field       = ('id')



