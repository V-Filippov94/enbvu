# Generated by Django 4.0.5 on 2022-06-20 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0007_alter_news_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['id'], 'verbose_name': 'Пункт меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_create'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]