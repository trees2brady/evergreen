# Generated by Django 3.2.8 on 2022-04-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20220412_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_delivery_man',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
