# Generated by Django 4.0.5 on 2022-07-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normativ_document', '0011_ustanovformy_exelustanovform'),
    ]

    operations = [
        migrations.AddField(
            model_name='exelustanovform',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название документа'),
            preserve_default=False,
        ),
    ]
