# Generated by Django 5.1.3 on 2024-11-09 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fill', '0002_remove_fill_dividendo_total_calculadividendos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculadividendos',
            name='fill',
        ),
        migrations.AddField(
            model_name='fill',
            name='fill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Fill.calculadividendos'),
            preserve_default=False,
        ),
    ]
