# Generated by Django 3.2.8 on 2022-04-20 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]