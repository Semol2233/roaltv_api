from django.urls import path
from .views import post_models
from django.conf.urls.static import static
from django.conf import settings
from roaltv_app import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
     path('',views.API_objects.as_view()),
     path('dtls/<id>/',views.dtls_view.as_view()),
     path('playlist',views.youtubevideos_playlist.as_view()),
     path('sports/<category>/',views.API_objedfcts.as_view()),
     path('moviecover',views.coverimg.as_view()),
     path('livetv_link',views.livetv_link.as_view()),
     
     path('latest',views.home_pagedata.as_view()),
     path('mostpopular',views.bareking_news.as_view()),
     path('breking_news',views.all_news.as_view()),
     path('shortplaylist',views.short_playlist.as_view()),
     path('about',views.about.as_view()),
     
]
 
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)