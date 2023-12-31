# Generated by Django 4.2.4 on 2023-08-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('c_location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Phone', 'Phone'), ('Tablet', 'Tablet'), ('Laptop', 'Laptop'), ('Other', 'Other')], max_length=50)),
                ('serial_number', models.CharField(max_length=100)),
                ('device_condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.IntegerField()),
                ('e_name', models.CharField(max_length=255)),
                ('e_email', models.EmailField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets_tracker.company')),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('condition_checkout', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tracking_records', to='Assets_tracker.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_tracking_records', to='Assets_tracker.employee')),
            ],
        ),
    ]
