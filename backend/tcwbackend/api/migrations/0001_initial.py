# Generated by Django 3.0.7 on 2020-06-18 10:29

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(default='Bicycle', max_length=50)),
                ('wheel_size', models.CharField(choices=[('size16', '16T'), ('size18', '18T'), ('size24', '24T'), ('size26', '26T'), ('size275', '27.5T'), ('size29', '29T'), ('freesize', 'Free Size')], default='Free Size', max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('speed', models.CharField(choices=[('speedsingle', 'Single Speed'), ('speed6', '6 Speed'), ('Speed7', '7 Speed'), ('speed12', '12 Speed'), ('speed18', '18 Speed'), ('speed21', '21 Speed'), ('speed24', '24 Speed')], default='Single Speed', max_length=100)),
                ('mrp', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('featured', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=True)),
                ('on_sale', models.BooleanField(default=False)),
                ('image1', models.ImageField(blank=True, upload_to=api.models.path_and_rename)),
                ('image2', models.ImageField(blank=True, upload_to=api.models.path_and_rename)),
                ('image3', models.ImageField(blank=True, upload_to=api.models.path_and_rename)),
                ('frame', models.CharField(blank=True, max_length=50)),
                ('fork', models.CharField(blank=True, max_length=50)),
                ('frame_material', models.CharField(blank=True, max_length=50)),
                ('saddle', models.CharField(blank=True, max_length=50)),
                ('rims', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('brakes', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, upload_to='uploads/brand_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('addr1', models.CharField(max_length=100)),
                ('addr2', models.CharField(max_length=100)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('orderStatus', models.CharField(choices=[('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('returned', 'Returned'), ('initiated', 'Initiated'), ('confirmed', 'Confirmed')], default='Initiated', max_length=15)),
                ('paymentStatus', models.CharField(default='Pending', max_length=15)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('payment_id', models.CharField(blank=True, max_length=60, null=True)),
                ('payment_transaction_id', models.CharField(blank=True, max_length=60, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('bicycle', models.ManyToManyField(to='api.Bicycle')),
            ],
        ),
        migrations.AddField(
            model_name='bicycle',
            name='brand',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='api.Brand'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='color',
            field=models.ManyToManyField(to='api.Color'),
        ),
    ]
