# Generated by Django 4.0.4 on 2022-06-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0002_alter_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.SlugField(max_length=300, unique=True, verbose_name='URL'),
        ),
    ]