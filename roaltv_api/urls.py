"""roaltv_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path,include
from admin_penel.views import listhome,PostCreateView,list_youtube,Profile
from atnBangla.views import atn_youtube_playlist,polls_detail,apps_coverimgview,short_playlist,livetvlisst,livetvdlts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('roaltv_app.urls')),





    path('log/',LoginView.as_view(),name='login'),
    path('home/',listhome.as_view(),name='homepage'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cre/', PostCreateView.as_view(), name='feede'),
    path('youtube', list_youtube.as_view(), name='yxsoutube'),
    path('pro/', Profile.as_view(), name='profile'),

    path('youtube_playlist/', atn_youtube_playlist.as_view()),
    path('img/', apps_coverimgview.as_view()),

    path('tvlist/', livetvlisst.as_view()),
    path('dtlspage/<id>/', livetvdlts.as_view()),
    path('homepage_playlist', short_playlist.as_view()),
    path('weblist', polls_detail),





]
