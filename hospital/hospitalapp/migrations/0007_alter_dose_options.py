# Generated by Django 4.0.4 on 2022-04-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0006_alter_dose_application_method'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dose',
            options={'ordering': ['-date']},
        ),
    ]
