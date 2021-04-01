# Generated by Django 3.1.6 on 2021-03-01 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Trello', '0002_auto_20210301_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 50, 17, 672035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='createdOn',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 15, 50, 17, 629040, tzinfo=utc)),
        ),
    ]