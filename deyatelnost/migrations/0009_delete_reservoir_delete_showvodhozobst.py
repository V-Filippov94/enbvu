# Generated by Django 4.0.5 on 2022-07-28 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deyatelnost', '0008_remove_reservoir_reservoir_boguch_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservoir',
        ),
        migrations.DeleteModel(
            name='ShowVodHozObst',
        ),
    ]