# Generated by Django 4.0.5 on 2022-07-13 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0045_delete_functionuprav_delete_polnomochiya'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionUprav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_function', models.TextField(verbose_name='Основные функции Управления')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_chenge', models.DateTimeField(verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Основную функцию Управления',
                'verbose_name_plural': '1.  Основные функции Управления  "(Функции и полномочия Енисейского БВУ)"',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Polnomochiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_polnomochiya', models.TextField(verbose_name='Полномочия')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_chenge', models.DateTimeField(verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Пункт полномочий',
                'verbose_name_plural': '1.1  Полномочия "(Функции и полномочия Енисейского БВУ)"',
                'ordering': ['id'],
            },
        ),
    ]
