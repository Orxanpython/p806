# Generated by Django 4.2.4 on 2023-10-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_tag_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
    ]