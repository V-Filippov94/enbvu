# Generated by Django 4.0.4 on 2022-06-29 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0021_unmenu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unmenu',
            options={'ordering': ['id'], 'verbose_name': 'Меню ПодПункт', 'verbose_name_plural': 'Меню ПодПункты'},
        ),
    ]