# Generated by Django 4.2.7 on 2023-11-21 14:35

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_options_alter_place_description_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='description_long',
        ),
        migrations.RemoveField(
            model_name='place',
            name='description_short',
        ),
        migrations.AddField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='long description'),
        ),
        migrations.AddField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='short description'),
        ),
        migrations.AlterField(
            model_name='image',
            name='priority',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0),
        ),
    ]
