# Generated by Django 3.2.9 on 2021-12-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoir', '0008_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage_of_expertise',
            field=models.IntegerField(),
        ),
    ]
