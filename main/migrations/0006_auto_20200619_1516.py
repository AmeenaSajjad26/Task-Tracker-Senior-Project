# Generated by Django 3.0.7 on 2020-06-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200619_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='estimatetime',
            new_name='spenttime',
        ),
    ]
