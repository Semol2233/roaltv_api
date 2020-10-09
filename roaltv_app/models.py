from django.db import models
from django.utils.translation import ugettext_lazy as _
class catgory_list(models.Model):
    cat_name           = models.CharField(max_length=255)
    release_date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.cat_name   



class post_models(models.Model):
    title          = models.CharField(max_length=255)
    catgory        = models.ManyToManyField(catgory_list,blank=True)
    description    = models.TextField(blank=True)
    release_date   = models.DateField(auto_now_add = True)
    # views          = models.IntegerField(blank=True, default=0)
    img_link      = models.URLField(max_length=400)

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = _("My Book")
        verbose_name_plural = _("My Books")

class youtube_videoplaylist(models.Model):
    playlist_name = models.CharField(max_length=255)
    channel_id    = models.CharField(max_length=800)
    playlist_code = models.CharField(max_length=800)

    def __str__(self):
        return self.playlist_name    


class movie_pageCover(models.Model):
    moviePgaecover = models.URLField(max_length=400)

    def __str__(self):
        return self.moviePgaecover    


class livetvlink(models.Model):
    livetv_link = models.URLField(max_length=400)

    def __str__(self):
        return self.livetv_link    




class about(models.Model):
    description    = models.TextField(blank=True)

    def __str__(self):
        return self.description    

class admove_ad_code(models.Model):
    ad_code    = models.TextField(blank=True)

    def __str__(self):
        return self.ad_code    

