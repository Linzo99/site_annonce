# Generated by Django 3.2 on 2021-04-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/<built-in function id>/%Y/%m/%d'),
        ),
    ]
