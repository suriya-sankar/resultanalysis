# Generated by Django 3.0.3 on 2020-03-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0013_batches_batch_year_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batches',
            name='batch_year_id',
            field=models.IntegerField(default=0),
        ),
    ]
