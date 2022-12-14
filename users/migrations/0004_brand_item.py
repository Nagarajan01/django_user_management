# Generated by Django 4.1.3 on 2022-11-21 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myuser_linkedin_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Apple', 'Apple'), ('Asus', 'Asus'), ('Oneplus', 'Oneplus'), ('Samsung', 'Samsung')], default='Electronics', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('in_stock', models.BooleanField(default=True)),
                ('brand', models.ManyToManyField(max_length=100, to='users.brand')),
            ],
        ),
    ]
