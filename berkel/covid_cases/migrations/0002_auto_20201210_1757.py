# Generated by Django 3.1.3 on 2020-12-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_cases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyreport',
            name='update',
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
