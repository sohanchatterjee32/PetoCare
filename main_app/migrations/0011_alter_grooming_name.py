# Generated by Django 3.2.5 on 2022-06-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_provider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grooming',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
