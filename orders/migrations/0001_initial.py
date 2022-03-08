# Generated by Django 3.2.8 on 2022-03-08 21:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dishes', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('finished_time', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishes')),
            ],
        ),
    ]
