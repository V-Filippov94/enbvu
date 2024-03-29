# Generated by Django 4.0.5 on 2022-08-02 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deyatelnost', '0012_region_alter_contentdeyatelnost_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrikazOZonePodtop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255, verbose_name='Название района')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deyatelnost.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Приказы об определении границы зоны затопления',
                'verbose_name_plural': 'Приказы об определении границы зоны затопления',
            },
        ),
    ]
