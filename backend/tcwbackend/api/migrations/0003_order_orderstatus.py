# Generated by Django 3.0.7 on 2020-06-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_order_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderStatus',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('returned', 'Returned'), ('initiated', 'Initiated'), ('confirmed', 'Confirmed')], default='Initiated', max_length=15),
        ),
    ]
