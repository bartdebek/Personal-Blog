# Generated by Django 4.0.3 on 2022-05-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoblog', '0016_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
