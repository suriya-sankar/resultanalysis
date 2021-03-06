# Generated by Django 3.0.3 on 2020-03-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=30)),
                ('starting_year', models.CharField(max_length=30)),
                ('ending_year', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('college', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
