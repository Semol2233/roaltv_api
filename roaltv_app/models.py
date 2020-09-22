from django.db import models

class catgory_list(models.Model):
    cat_name           = models.CharField(max_length=255)
    release_date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.cat_name   



class post_models(models.Model):
    title          = models.CharField(max_length=255)
    catgory        = models.ForeignKey(catgory_list,on_delete=models.CASCADE ,blank=True)
    description    = models.TextField(blank=True)
    release_date   = models.DateField(auto_now_add = True)
    # views          = models.IntegerField(blank=True, default=0)
    img_link      = models.URLField(max_length=400)

    def __str__(self):
        return self.title    