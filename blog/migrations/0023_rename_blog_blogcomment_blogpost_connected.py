# Generated by Django 3.2 on 2022-02-09 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='blog',
            new_name='blogpost_connected',
        ),
    ]