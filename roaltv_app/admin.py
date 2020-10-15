from django.contrib import admin

admin.site.site_header = "NXT-1.0 - ATN BANGLA"

class post_modelsAdmin(admin.ModelAdmin):
    list_display = ('id','title','release_date')
    list_filter = ('title', )
    search_fields = ("title__startswith", )

    

from .models import *
# admin.site.register(post_models ,post_modelsAdmin)
# admin.site.register(catgory_list)
# admin.site.register(youtube_videoplaylist)
# admin.site.register(movie_pageCover)
# admin.site.register(livetvlink)
# admin.site.register(about)
admin.site.register(Profile)
admin.site.register(apps_coverimg)
admin.site.register(livetvlist)
admin.site.register(youtube_videoplaylist_atn)
admin.site.register(liveweblisttvlist)






