# Generated by Django 4.2.17 on 2024-12-08 13:08

from django.db import migrations, models
import vlog.models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlogpost',
            name='tags',
            field=models.CharField(blank=True, help_text='Enter tags separated by spaces', max_length=200),
        ),
        migrations.AlterField(
            model_name='vlogpost',
            name='video_url',
            field=models.URLField(help_text='Enter a YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)', validators=[vlog.models.validate_youtube_url]),
        ),
    ]
