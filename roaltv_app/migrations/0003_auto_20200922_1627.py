# Generated by Django 3.1.1 on 2020-09-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaltv_app', '0002_auto_20200922_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_models',
            name='img',
        ),
        migrations.AddField(
            model_name='post_models',
            name='img_link',
            field=models.URLField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
