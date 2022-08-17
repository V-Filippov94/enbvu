# Generated by Django 4.0.5 on 2022-07-14 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0050_remove_phoneorganization_organization_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование организации')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('address_cor', models.TextField(blank=True, verbose_name='Адрес для корреспонденции')),
                ('mode', models.CharField(blank=True, max_length=300, verbose_name='Режим работы')),
                ('fax', models.CharField(blank=True, max_length=20, verbose_name='Факс')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Email')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Организацию',
                'verbose_name_plural': '3.1 Организация ("Структура управления")',
            },
        ),
        migrations.CreateModel(
            name='SectorOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=355, verbose_name='Отдел')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО сотрудника')),
                ('post', models.CharField(max_length=255, verbose_name='Должность')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization', verbose_name='Организация')),
                ('sector_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.sectororganization', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Сотрудника',
                'verbose_name_plural': '3.2 Сотрудники ("Структура управления")',
            },
        ),
        migrations.CreateModel(
            name='PhoneWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Телефон сотрудника')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.worker')),
            ],
            options={
                'verbose_name': 'Телефон сотрудника',
                'verbose_name_plural': 'Телефоны сотрудника',
            },
        ),
        migrations.CreateModel(
            name='PhoneOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Телефон организации')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization')),
            ],
            options={
                'verbose_name': 'Телефоны организации',
                'verbose_name_plural': 'Телефон организации',
            },
        ),
    ]