# Generated by Django 3.0.7 on 2020-07-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200619_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.AlterField(
            model_name='task',
            name='spenttime',
            field=models.PositiveIntegerField(default=0),
        ),
    ]