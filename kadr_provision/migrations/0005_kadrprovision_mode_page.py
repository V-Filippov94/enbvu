# Generated by Django 4.0.5 on 2022-08-04 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0090_alter_content_options'),
        ('kadr_provision', '0004_listfilekadr_filekadr'),
    ]

    operations = [
        migrations.AddField(
            model_name='kadrprovision',
            name='mode_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.modepage', verbose_name='Вид контекста'),
            preserve_default=False,
        ),
    ]
