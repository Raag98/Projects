# Generated by Django 3.1.6 on 2021-03-05 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trello', '0004_auto_20210302_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='createdOn',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
