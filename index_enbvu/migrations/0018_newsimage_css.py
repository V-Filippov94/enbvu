# Generated by Django 4.0.5 on 2022-06-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0017_remove_news_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsimage',
            name='css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
    ]