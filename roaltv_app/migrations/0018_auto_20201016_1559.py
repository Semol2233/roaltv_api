# Generated by Django 2.2.5 on 2020-10-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaltv_app', '0017_about_atn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admove_ad_code',
            old_name='ad_code',
            new_name='Ads_SDK_id',
        ),
        migrations.AddField(
            model_name='admove_ad_code',
            name='ads_code',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='admove_ad_code',
            name='ads_page',
            field=models.CharField(blank=True, choices=[('home_page_banner_ad', 'home_page_banner_ad'), ('youtube_page', 'youtube_page'), ('home_page_bottom_ads', 'global_bottom_page_ads'), ('home_page_bottom_ads', 'home_web_tabs_ads'), ('home_page_bottom_ads', 'home_youtube_tabs_ads')], default='home_page_banner_ad', max_length=10),
        ),
    ]
