# Generated by Django 3.2.12 on 2022-04-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_auto_20220427_0915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examination',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='hospitalization',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_strenght',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Strength(mg)'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
