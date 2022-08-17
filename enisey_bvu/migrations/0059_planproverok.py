# Generated by Django 4.0.5 on 2022-07-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0058_delete_planproverok'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanProverok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'План проверок',
                'verbose_name_plural': '7. План проверок, результаты проверок',
                'ordering': ['id'],
            },
        ),
    ]
