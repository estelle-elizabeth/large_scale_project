# Generated by Django 2.2.7 on 2019-12-10 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191209_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_truck',
            name='truck_id',
        ),
    ]
