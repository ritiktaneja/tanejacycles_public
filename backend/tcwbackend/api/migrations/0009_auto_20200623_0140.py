# Generated by Django 3.0.7 on 2020-06-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200622_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='speed',
            field=models.CharField(choices=[('speedsingle', 'Single Speed'), ('speed6', '6 Speed'), ('speed7', '7 Speed'), ('speed12', '12 Speed'), ('speed18', '18 Speed'), ('speed21', '21 Speed'), ('speed24', '24 Speed')], default='Single Speed', max_length=100),
        ),
    ]
