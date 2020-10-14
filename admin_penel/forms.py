from django import forms
from roaltv_app.models import *

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = videomo
#         fields = ['title','clip','photo']
#         widgets = {
#             'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
#         }

class PostNews(forms.ModelForm):
    class Meta:
        model = youtube_videoplaylist
        fields = ['playlist_name','channel_id','playlist_code']
        widgets = {
            'playlist_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'channel_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
            'playlist_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}),
        }
