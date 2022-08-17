# Generated by Django 4.0.5 on 2022-08-04 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0090_alter_content_options'),
        ('kadr_provision', '0003_remove_kadrprovision_mode_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListFileKadr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Текст (пояснение к файлу)')),
                ('kadr_provision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kadr_provision.kadrprovision')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Добавить список файлов',
            },
        ),
        migrations.CreateModel(
            name='FileKadr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название файла')),
                ('file', models.FileField(blank=True, upload_to='deyatelnost/kadry/files', verbose_name='Файл')),
                ('kadr_provision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kadr_provision.kadrprovision')),
                ('list_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kadr_provision.listfilekadr', verbose_name='Пояснение к файлу')),
                ('picture_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.picturefile', verbose_name='Расширение файла')),
            ],
            options={
                'verbose_name': 'Файл',
            },
        ),
    ]
