# Generated by Django 4.0.5 on 2022-07-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0036_infozakupki'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanProverok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'План проверок',
                'verbose_name_plural': '6. План проверок, результаты проверок',
            },
        ),
        migrations.AlterModelOptions(
            name='infozakupki',
            options={'verbose_name': 'Статью закупки', 'verbose_name_plural': '5. Информация об осуществлении закупок товаров, работ, услуг для государственных нужд'},
        ),
    ]