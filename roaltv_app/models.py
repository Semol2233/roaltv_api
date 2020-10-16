from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# class admin_user(models.Model):
#     username = models.for
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
class catgory_list(models.Model):
    cat_name           = models.CharField(max_length=255)
    release_date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.cat_name   

    class Meta:
        verbose_name = _("Create Category")
        verbose_name_plural = _("Create Category")

class post_models(models.Model):
    title          = models.CharField(max_length=255)
    catgory        = models.ManyToManyField(catgory_list,blank=True)
    description    = models.TextField(blank=True)
    release_date   = models.DateField(auto_now_add = True)
    # views          = models.IntegerField(blank=True, default=0)
    img_link      = models.URLField(max_length=400)

    def __str__(self):
        return self.title    

    # def get_absolute_url(self):
    #     return reverse('home')




    class Meta:
        verbose_name = _("Post News")
        verbose_name_plural = _("Post News")

class youtube_videoplaylist(models.Model):
    playlist_name = models.CharField(max_length=255)
    channel_id    = models.CharField(max_length=800)
    playlist_code = models.CharField(max_length=800)

    def __str__(self):
        return self.playlist_name    
    class Meta:
        verbose_name = _("Create YouTube PlayList")
        verbose_name_plural = _("Create YouTube PlayList")

    def get_absolute_url(self):
        return reverse('yxsoutube')


class movie_pageCover(models.Model):
    moviePgaecover = models.URLField(max_length=400)

    def __str__(self):
        return self.moviePgaecover    

    class Meta:
        verbose_name = _("Cover Img")
        verbose_name_plural = _("Cover Img")


class livetvlink(models.Model):
    livetv_link = models.URLField(max_length=400)

    def __str__(self):
        return self.livetv_link    
    class Meta:
        verbose_name = _("Live Tv Url")
        verbose_name_plural = _("Live Tv Url")



class about(models.Model):
    description    = models.TextField(blank=True)

    def __str__(self):
        return self.description    
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About")



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileimg = models.URLField(max_length=400)
    create = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.user    


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




# Atn_part


class admove_ad_code(models.Model):
    home_page_banner_ad = 'home_page_banner_ad'
    youtube_page = 'youtube_page'
    global_bottom_page_ads = 'home_page_bottom_ads'
    home_web_tabs_ads = 'home_page_bottom_ads'
    home_youtube_tabs_ads = 'home_page_bottom_ads'



    CHOICES = (
        (home_page_banner_ad, "home_page_banner_ad"),
        (youtube_page, "youtube_page"),
        (global_bottom_page_ads, "global_bottom_page_ads"),
        (home_web_tabs_ads, "home_web_tabs_ads"),
        (home_youtube_tabs_ads, "home_youtube_tabs_ads")

    )
    ads_page = models.CharField(max_length=200, choices = CHOICES,default=home_page_banner_ad,blank=True)
    Ads_SDK_id  = models.TextField(blank=True)
    ads_code    = models.TextField(blank=True)


    def __str__(self):
        return self.ads_page    
    class Meta:
        verbose_name = _("AdMob")
        verbose_name_plural = _("AdMob")


class apps_coverimg(models.Model):
    Specfiction = 'home'
    Review = 'youtube'
    CHOICES = (
        (Specfiction, "homepage"),
        (Review, "youtube_page"),
    )
    moviePgaecover = models.URLField(max_length=400)
    typeimg = models.CharField(max_length=10, choices = CHOICES,default=Review,blank=True)

    def __str__(self):
        return self.typeimg 
    class Meta:
        verbose_name = _("cover img")
        verbose_name_plural = _("cover img")


class youtube_videoplaylist_atn(models.Model):
    playlist_name = models.CharField(max_length=255)
    channel_id    = models.CharField(max_length=800)
    playlist_code = models.CharField(max_length=800)

    def __str__(self):
        return self.playlist_name    
    class Meta:
        verbose_name = _("Create YouTube PlayList")
        verbose_name_plural = _("Create YouTube PlayList")



class livetvlist(models.Model):
    channe_name    = models.CharField(max_length=100)
    channel_logo   =  models.URLField(max_length=400)
    channel_tvurl  =  models.URLField(max_length=400)
    release_date   = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = _("Create livetv")
        verbose_name_plural = _("Create livetv")



class liveweblisttvlist(models.Model):
    channel_logo   =  models.URLField(max_length=400)
    web_link  =  models.URLField(max_length=400)
    release_date   = models.DateField(auto_now_add = True)

    class Meta:
        verbose_name = _("Create Weblist")
        verbose_name_plural = _("Create Weblist")






class about_atn(models.Model):
    description    = models.TextField(blank=True)

    def __str__(self):
        return self.description    
    class Meta:
        verbose_name = _("Apps About")
        verbose_name_plural = _("Apps About")
