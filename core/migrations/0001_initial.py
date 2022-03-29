# Generated by Django 4.0.3 on 2022-03-29 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning', models.BooleanField(verbose_name=False)),
                ('afternoon', models.BooleanField(verbose_name=False)),
                ('evening', models.BooleanField(verbose_name=False)),
                ('shift_started', models.TimeField(blank=True, null=True)),
                ('shift_ended', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_set', models.BooleanField(verbose_name=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.worker')),
            ],
        ),
    ]
