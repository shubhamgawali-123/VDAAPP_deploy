# Generated by Django 3.1.3 on 2020-11-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VinNumber',
            fields=[
                ('vinNumber', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('VDAFile', models.FileField(upload_to='')),
            ],
        ),
    ]
