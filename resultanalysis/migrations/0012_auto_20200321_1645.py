# Generated by Django 3.0.3 on 2020-03-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0011_auto_20200321_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='excel_raw_data',
            name='batch_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='excel_raw_data',
            name='batch_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='excel_raw_data',
            name='sem_id',
            field=models.IntegerField(default=1),
        ),
    ]
