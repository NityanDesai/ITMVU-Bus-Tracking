# Generated by Django 3.1.3 on 2021-04-17 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('bus_route_no', models.IntegerField(primary_key=True, serialize=False)),
                ('role_id', models.IntegerField(blank=True, default='0')),
                ('driver_mobile_no', models.BigIntegerField()),
                ('driver_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bus',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=103),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bus',
            name='driver_mobile_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='parent_mobile_no',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roll_no',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
