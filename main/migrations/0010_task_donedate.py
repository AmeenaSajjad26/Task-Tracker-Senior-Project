# Generated by Django 3.0.7 on 2020-07-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200708_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='donedate',
            field=models.DateField(null=True),
        ),
    ]
