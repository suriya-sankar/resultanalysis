# Generated by Django 3.0.3 on 2020-03-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0012_auto_20200321_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='batches',
            name='batch_year_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
