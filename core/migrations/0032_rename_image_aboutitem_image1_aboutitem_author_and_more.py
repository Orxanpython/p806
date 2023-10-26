# Generated by Django 4.2.4 on 2023-10-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutitem',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='aboutitem',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutitem',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutitem',
            name='image2',
            field=models.ImageField(default=1, upload_to='about_images/'),
            preserve_default=False,
        ),
    ]