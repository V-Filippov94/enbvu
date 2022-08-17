# Generated by Django 4.0.5 on 2022-07-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0054_delete_perechniinfosistembvu'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerechniInfoSistemBVU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': '5. Перечни информационных систем, банков данных, реестров, регистров, находящихся в ведении Енисейского БВУ',
            },
        ),
    ]