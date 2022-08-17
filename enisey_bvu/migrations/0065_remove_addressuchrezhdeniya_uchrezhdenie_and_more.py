# Generated by Django 4.0.5 on 2022-07-18 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0064_alter_organization_options_alter_worker_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressuchrezhdeniya',
            name='uchrezhdenie',
        ),
        migrations.DeleteModel(
            name='FunctionUprav',
        ),
        migrations.DeleteModel(
            name='InfoZakupki',
        ),
        migrations.DeleteModel(
            name='NormAktFunction',
        ),
        migrations.DeleteModel(
            name='OficialVystup',
        ),
        migrations.DeleteModel(
            name='PerechniInfoSistemBVU',
        ),
        migrations.RemoveField(
            model_name='phoneorganization',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='phoneuchrezhdeniya',
            name='address',
        ),
        migrations.RemoveField(
            model_name='phoneuchrezhdeniya',
            name='uchrezhdenie',
        ),
        migrations.RemoveField(
            model_name='phoneworker',
            name='worker',
        ),
        migrations.DeleteModel(
            name='PlanProverok',
        ),
        migrations.DeleteModel(
            name='Polnomochiya',
        ),
        migrations.RemoveField(
            model_name='sectororganization',
            name='organization',
        ),
        migrations.DeleteModel(
            name='SvedeniyaSmi',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='sector_organization',
        ),
        migrations.DeleteModel(
            name='AddressUchrezhdeniya',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='PhoneOrganization',
        ),
        migrations.DeleteModel(
            name='PhoneUchrezhdeniya',
        ),
        migrations.DeleteModel(
            name='PhoneWorker',
        ),
        migrations.DeleteModel(
            name='SectorOrganization',
        ),
        migrations.DeleteModel(
            name='Uchrezhdeniya',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
