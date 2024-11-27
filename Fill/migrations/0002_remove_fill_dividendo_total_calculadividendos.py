# Generated by Django 5.1.3 on 2024-11-08 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fill', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fill',
            name='dividendo_total',
        ),
        migrations.CreateModel(
            name='CalculaDividendos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dividendo_total', models.FloatField(blank=True, null=True)),
                ('fill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fill.fill')),
            ],
            options={
                'ordering': ['dividendo_total'],
            },
        ),
    ]
