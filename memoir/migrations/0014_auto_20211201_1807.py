# Generated by Django 3.2.9 on 2021-12-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoir', '0013_auto_20211201_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='hire_me_url',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='banner',
            name='read_more_url',
            field=models.CharField(max_length=600),
        ),
    ]