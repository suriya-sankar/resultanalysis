# Generated by Django 3.0.3 on 2020-03-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0007_auto_20200320_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batches',
            name='batch_name',
            field=models.CharField(blank=True, default='not specified', max_length=30),
        ),
        migrations.AlterField(
            model_name='batches',
            name='college',
            field=models.CharField(blank=True, default='not specified', max_length=50),
        ),
        migrations.AlterField(
            model_name='batches',
            name='description',
            field=models.TextField(blank=True, default='not specified'),
        ),
    ]
