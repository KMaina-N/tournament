# Generated by Django 4.2.7 on 2023-11-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_tounament_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='opponent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
