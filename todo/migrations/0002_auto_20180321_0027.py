# Generated by Django 2.0 on 2018-03-20 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='compelete',
            new_name='complete',
        ),
    ]
