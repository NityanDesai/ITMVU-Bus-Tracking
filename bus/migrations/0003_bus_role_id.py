# Generated by Django 3.1.3 on 2021-04-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0002_auto_20210417_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='role_id',
            field=models.IntegerField(blank=True, default='1'),
        ),
    ]