# Generated by Django 4.0.5 on 2022-07-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0014_organization_alter_functionuprav_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address_cor',
            field=models.TextField(blank=True, verbose_name='Адрес для корреспонденции'),
        ),
    ]