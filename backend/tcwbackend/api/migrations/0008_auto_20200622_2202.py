# Generated by Django 3.0.7 on 2020-06-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_suborder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suborder',
            old_name='price',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bicycle',
        ),
    ]