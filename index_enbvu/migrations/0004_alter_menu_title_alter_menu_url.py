# Generated by Django 4.0.4 on 2022-06-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0003_alter_menu_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.SlugField(max_length=250, unique=True, verbose_name='URL'),
        ),
    ]
