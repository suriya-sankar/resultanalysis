# Generated by Django 3.0.3 on 2020-03-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0017_auto_20200322_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batches',
            name='department',
            field=models.CharField(blank=True, choices=[('cse', 'cse'), ('eee', 'eee'), ('ece', 'ece'), ('aero', 'aero')], max_length=20),
        ),
        migrations.AlterField(
            model_name='semester_result_data',
            name='register_no',
            field=models.IntegerField(default=0),
        ),
    ]
