# Generated by Django 3.2 on 2021-04-25 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0019_auto_20210425_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seats',
            old_name='present_in_theater',
            new_name='theater',
        ),
    ]
