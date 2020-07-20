# Generated by Django 3.0.8 on 2020-07-20 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='NULL', max_length=30, verbose_name='Employee Name')),
                ('designation', models.CharField(choices=[('Worker', 'Worker'), ('Manager', 'Manager'), ('Superviser', 'Superviser'), ('MarketingHead', 'MarketingHead'), ('Worker', 'others')], default='Others', max_length=200)),
                ('address', models.CharField(blank=True, default='Not Found', max_length=70)),
                ('phone', models.CharField(blank=True, default='0000000', max_length=11, verbose_name='Phone Number')),
                ('dob', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date of birth')),
                ('doj', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date of Joined')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (1, 'Others')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Product Name')),
                ('cost', models.IntegerField(default=0, verbose_name='Cost per Kg')),
                ('wages', models.DecimalField(decimal_places=3, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateTimeField(verbose_name='date of salary updated')),
            ],
        ),
    ]
