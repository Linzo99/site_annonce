# Generated by Django 3.2 on 2021-04-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_jourj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
