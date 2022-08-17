# Generated by Django 4.0.5 on 2022-07-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0042_svedeniyasmi_alter_oficialvystup_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerechniInfoSistemBVU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Статью закупки',
                'verbose_name_plural': '5. Перечни информационных систем, банков данных, реестров, регистров, находящихся в ведении Енисейского БВУ',
            },
        ),
        migrations.AlterModelOptions(
            name='infozakupki',
            options={'verbose_name': 'Статью закупки', 'verbose_name_plural': '6. Информация об осуществлении закупок товаров, работ, услуг для государственных нужд'},
        ),
        migrations.AlterModelOptions(
            name='oficialvystup',
            options={'verbose_name': 'Официальное выступление или заявление', 'verbose_name_plural': '8.  Официальные выступления и заявления'},
        ),
        migrations.AlterModelOptions(
            name='planproverok',
            options={'ordering': ['id'], 'verbose_name': 'План проверок', 'verbose_name_plural': '7. План проверок, результаты проверок'},
        ),
        migrations.AlterModelOptions(
            name='svedeniyasmi',
            options={'verbose_name': 'Сведения о финансировании (отсутсвии финансирования) средств массовой информации', 'verbose_name_plural': '9.  Сведения о финансировании (отсутсвии финансирования) средств массовой информации'},
        ),
    ]