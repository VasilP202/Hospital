# Generated by Django 3.2.12 on 2022-04-27 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_auto_20220427_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='dose',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]