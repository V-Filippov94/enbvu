# Generated by Django 4.0.5 on 2022-07-07 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0008_remove_phoneworker_worker_remove_worker_organization_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название организации')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('address_cor', models.TextField(blank=True, verbose_name='Адрес для корреспонденции')),
                ('mode', models.CharField(max_length=255, verbose_name='Режим работы')),
            ],
            options={
                'verbose_name': 'Организацию',
                'verbose_name_plural': 'Структура управления',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО сотрудника')),
                ('post', models.CharField(max_length=300, verbose_name='Должность')),
                ('fax', models.CharField(blank=True, max_length=255, verbose_name='Факс')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Email')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=255, verbose_name='Телефон')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.worker')),
            ],
        ),
    ]
