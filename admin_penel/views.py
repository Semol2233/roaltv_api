from roaltv_app.models import *
from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse,reverse_lazy
from django.db.models import Q 
from django.shortcuts import get_object_or_404

# def homeview(request):
#     return render(request,'registration/home.html')



class listhome(LoginRequiredMixin,ListView):
    context_object_name = 'listdata'
    model = post_models
    template_name= 'home.html'
    queryset = post_models.objects.all()

class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostNews
    model = youtube_videoplaylist
    template_name = 'uplode_news.html'

class list_youtube(LoginRequiredMixin,ListView):
    context_object_name = 'listyoutube'
    model = youtube_videoplaylist
    template_name= 'youtubevideolist.html'
    queryset = youtube_videoplaylist.objects.all()




class Profile(DetailView):
    context_object_name = 'listdata'
    template_name = 'user.html'
    queryset = Profile.objects.all()


