# Generated by Django 4.1.3 on 2022-11-22 10:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_brand_brand_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=0)),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Received', 'Received'), ('Scheduled', 'Scheduled'), ('Shipped', 'Shipped'), ('Failed', 'Failed'), ('In Progress', 'In Progress')], default='In Progress', max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField(default=0)),
                ('items', models.ManyToManyField(to='users.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
