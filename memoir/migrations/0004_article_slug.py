# Generated by Django 3.2.9 on 2021-11-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoir', '0003_auto_20211124_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='ho'),
        ),
    ]
