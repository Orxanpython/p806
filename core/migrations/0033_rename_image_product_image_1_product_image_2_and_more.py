# Generated by Django 4.2.4 on 2023-10-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_rename_image_aboutitem_image1_aboutitem_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
    ]