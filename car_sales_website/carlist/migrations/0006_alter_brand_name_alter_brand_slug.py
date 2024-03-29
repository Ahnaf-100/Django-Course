# Generated by Django 5.0 on 2024-02-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlist', '0005_alter_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
