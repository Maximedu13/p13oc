# Generated by Django 2.2.3 on 2019-08-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikibsteros', '0014_auto_20190825_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='mother',
            field=models.CharField(default='', max_length=200),
        ),
    ]
