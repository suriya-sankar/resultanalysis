# Generated by Django 3.0.3 on 2020-03-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0018_auto_20200322_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='came',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_data', models.FileField(upload_to='')),
            ],
        ),
    ]
