# Generated by Django 3.2 on 2021-04-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
