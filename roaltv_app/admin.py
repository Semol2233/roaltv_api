from django.contrib import admin

admin.site.site_header = "RoalTv"


class Post_models(admin.ModelAdmin):
    list_display = ('title', 'catgory','release_date')
    list_filter = ('mfg_date', )

from .models import *
admin.site.register(post_models)
admin.site.register(catgory_list)
admin.site.register(youtube_videoplaylist)
admin.site.register(movie_pageCover)
admin.site.register(livetvlink)
admin.site.register(about)


