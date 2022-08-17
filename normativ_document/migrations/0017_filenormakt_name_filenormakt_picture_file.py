# Generated by Django 4.0.5 on 2022-07-26 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enisey_bvu', '0088_file_picture_file_alter_file_name'),
        ('normativ_document', '0016_alter_filenormakt_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='filenormakt',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Название файла'),
        ),
        migrations.AddField(
            model_name='filenormakt',
            name='picture_file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.picturefile', verbose_name='Расширение файла'),
            preserve_default=False,
        ),
    ]