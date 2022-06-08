# Generated by Django 3.2.5 on 2022-06-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_vet_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.IntegerField(primary_key='True', serialize=False)),
                ('service_type', models.CharField(max_length=20)),
                ('service_desc', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
            ],
        ),
    ]
