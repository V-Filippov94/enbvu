# Generated by Django 4.0.5 on 2022-06-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enisey_bvu', '0002_delete_normativakt'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionUprav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_function', models.TextField(verbose_name='Основные функции Управления')),
            ],
            options={
                'verbose_name': 'Основные функции Управления',
                'verbose_name_plural': 'Основные функции Управления',
                'ordering': ['id'],
            },
        ),
    ]