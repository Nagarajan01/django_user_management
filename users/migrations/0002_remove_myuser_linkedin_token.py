# Generated by Django 4.1.3 on 2022-11-18 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='linkedin_token',
        ),
    ]
