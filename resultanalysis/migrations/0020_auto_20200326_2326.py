# Generated by Django 3.0.3 on 2020-03-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0019_came'),
    ]

    operations = [
        migrations.CreateModel(
            name='arrears_excel_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(blank=True, max_length=30)),
                ('batch_id', models.IntegerField(default=1)),
                ('sem_id', models.IntegerField(default=1)),
                ('arrear_sem_id', models.IntegerField(default=1)),
                ('excel_data', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='semester_result_data',
        ),
    ]
