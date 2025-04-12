# Generated by Django 5.0.4 on 2025-04-11 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0002_parkingrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='parkingrequest',
            name='guard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_app.guard'),
        ),
    ]
