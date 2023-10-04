# Generated by Django 4.2.4 on 2023-10-01 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_shopproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopproduct',
            options={},
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='created_at',
            field=models.DateTimeField(default=datetime.timezone),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop'),
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
