# Generated by Django 4.2.1 on 2023-05-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
