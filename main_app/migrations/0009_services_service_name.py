# Generated by Django 3.2.5 on 2022-06-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_servicebooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]