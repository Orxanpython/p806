# Generated by Django 4.2.4 on 2023-10-01 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_shopproduct_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]