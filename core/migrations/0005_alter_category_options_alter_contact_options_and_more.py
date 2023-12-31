# Generated by Django 4.2.4 on 2023-09-13 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_category_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
    ]
