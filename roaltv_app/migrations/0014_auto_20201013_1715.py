# Generated by Django 3.1.1 on 2020-10-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaltv_app', '0013_auto_20201013_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps_coverimg',
            name='typeimg',
            field=models.CharField(blank=True, choices=[('home', 'homepage'), ('youtube', 'youtube_page')], default='youtube', max_length=10),
        ),
    ]
