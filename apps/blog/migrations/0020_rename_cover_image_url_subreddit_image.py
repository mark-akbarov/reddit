# Generated by Django 3.2 on 2022-02-09 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_subreddit_cover_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subreddit',
            old_name='cover_image_url',
            new_name='image',
        ),
    ]