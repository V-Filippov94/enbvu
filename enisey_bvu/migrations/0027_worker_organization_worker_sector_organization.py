# Generated by Django 4.0.5 on 2022-07-08 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0026_remove_worker_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.organization', verbose_name='Организация'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='sector_organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.sectororganization', verbose_name='Отдел'),
            preserve_default=False,
        ),
    ]
