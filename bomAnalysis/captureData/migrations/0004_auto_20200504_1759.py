# Generated by Django 3.0.5 on 2020-05-04 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('captureData', '0003_auto_20200504_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]