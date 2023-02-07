from django.db import migrations


def create_departments(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Department = apps.get_model('hospitalapp', 'Department')
    Department.objects.using(db_alias).bulk_create([
        Department(icpe='10015915', title='Surgery'),
        Department(icpe='73261760', title='Intensive care'),
        Department(icpe='15632144', title='Gynecology'),
        Department(icpe='64013211', title='Neurology'),
        Department(icpe='28025943', title='Ophthalmology'),
        Department(icpe='54289911', title='Orthopaedics'),

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_departments),
    ]
