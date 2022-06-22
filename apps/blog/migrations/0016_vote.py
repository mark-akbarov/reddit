# Generated by Django 3.2 on 2022-02-07 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20220207_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='blogid', to='blog.blog')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='blog.blog')),
            ],
        ),
    ]