# Generated by Django 2.2.3 on 2019-10-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikibsteros', '0022_votescharacters'),
    ]

    operations = [
        migrations.AddField(
            model_name='votescharacters',
            name='note',
            field=models.FloatField(default=1.0),
        ),
    ]
