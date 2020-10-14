# Generated by Django 3.1.1 on 2020-10-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaltv_app', '0011_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='apps_coverimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviePgaecover', models.URLField(max_length=400)),
                ('howpage', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Home page cover img',
                'verbose_name_plural': 'Home page cover img',
            },
        ),
        migrations.CreateModel(
            name='youtube_videoplaylist_atn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=255)),
                ('channel_id', models.CharField(max_length=800)),
                ('playlist_code', models.CharField(max_length=800)),
            ],
            options={
                'verbose_name': 'Create YouTube PlayList',
                'verbose_name_plural': 'Create YouTube PlayList',
            },
        ),
        migrations.AlterModelOptions(
            name='admove_ad_code',
            options={'verbose_name': 'AdMob code', 'verbose_name_plural': 'AdMob code'},
        ),
    ]
