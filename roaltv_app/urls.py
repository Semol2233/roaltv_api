from django.urls import path
from .views import post_models
from django.conf.urls.static import static
from django.conf import settings
from roaltv_app import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
     path('',views.API_objects.as_view()),
     path('dtls/<id>/',views.dtls_view.as_view())


     
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)