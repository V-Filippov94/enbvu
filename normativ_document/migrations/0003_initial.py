# Generated by Django 4.0.5 on 2022-07-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('normativ_document', '0002_delete_normaktrosvod'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormAktRosvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Текст статьи',
                'verbose_name_plural': '1. Нормативные правовые акты, изданные Федеральным агентством водных ресурсов',
            },
        ),
    ]
