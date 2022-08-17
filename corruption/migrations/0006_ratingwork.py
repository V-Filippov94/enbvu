# Generated by Django 4.0.5 on 2022-08-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corruption', '0005_delete_ratingwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high', models.BooleanField(default=False, verbose_name='Высокий уровень')),
                ('average', models.BooleanField(default=False, verbose_name='Средний уровень')),
                ('short', models.BooleanField(default=False, verbose_name='Низкий уровень')),
            ],
        ),
    ]
