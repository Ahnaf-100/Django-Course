# Generated by Django 5.0 on 2024-02-13 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlist', '0007_alter_brand_name_alter_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
