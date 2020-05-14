# Generated by Django 3.0.3 on 2020-03-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0016_remove_semester_result_data_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='sem_subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.IntegerField(default=0)),
                ('sem_id', models.IntegerField(default=0)),
                ('department', models.CharField(default='none', max_length=100)),
                ('sub_1_name', models.CharField(blank=True, max_length=30)),
                ('sub_2_name', models.CharField(blank=True, max_length=30)),
                ('sub_3_name', models.CharField(blank=True, max_length=30)),
                ('sub_4_name', models.CharField(blank=True, max_length=30)),
                ('sub_5_name', models.CharField(blank=True, max_length=30)),
                ('sub_6_name', models.CharField(blank=True, max_length=30)),
                ('lab_1_name', models.CharField(blank=True, max_length=30)),
                ('lab_2_name', models.CharField(blank=True, max_length=30)),
                ('lab_3_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='lab_1_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='lab_2_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='lab_3_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_1_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_2_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_3_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_4_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_5_name',
        ),
        migrations.RemoveField(
            model_name='semester_result_data',
            name='sub_6_name',
        ),
    ]