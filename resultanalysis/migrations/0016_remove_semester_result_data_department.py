# Generated by Django 3.0.3 on 2020-03-21 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0015_semester_result_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester_result_data',
            name='department',
        ),
    ]
