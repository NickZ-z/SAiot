# Generated by Django 4.2.5 on 2023-09-13 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('number_door', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('door', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='door_device.doors')),
            ],
        ),
    ]