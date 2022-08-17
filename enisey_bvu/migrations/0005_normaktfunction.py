# Generated by Django 4.0.5 on 2022-07-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0004_polnomochiya_alter_functionuprav_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormAktFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название документа')),
                ('url_doc', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на документ')),
                ('file_pdf', models.FileField(blank=True, upload_to='enisey_bvu/normativnye_akty_function', verbose_name='Документ')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Нормативные акты, определяющие полномочия, задачи и функции',
                'ordering': ['id'],
            },
        ),
    ]
