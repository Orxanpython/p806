# Generated by Django 4.2.4 on 2023-10-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
