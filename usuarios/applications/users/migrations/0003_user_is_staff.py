# Generated by Django 3.2.9 on 2021-12-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211214_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
