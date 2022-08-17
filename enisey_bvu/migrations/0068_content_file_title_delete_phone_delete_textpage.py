# Generated by Django 4.0.5 on 2022-07-18 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0040_alter_mirvodyimage_options_alter_newsfilepdf_options_and_more'),
        ('enisey_bvu', '0067_phone_remove_textpage_un_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст страницы')),
                ('date_created', models.DateTimeField(verbose_name='Дата добавления')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('unMenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.unmenu')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_pdf', models.FileField(blank=True, upload_to='enisey_bvu/file_pdf', verbose_name='Файл PDF')),
                ('file', models.FileField(blank=True, upload_to='enisey_bvu/file_all', verbose_name='Все файлы')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.content')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Заголовок')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.content')),
            ],
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.DeleteModel(
            name='TextPage',
        ),
    ]