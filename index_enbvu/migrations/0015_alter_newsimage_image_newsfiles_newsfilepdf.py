# Generated by Django 4.0.5 on 2022-06-21 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0014_newsimage_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='index_enbvu/', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='NewsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='files/', verbose_name='Файл')),
                ('news_file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index_enbvu.news')),
            ],
        ),
        migrations.CreateModel(
            name='NewsFilePDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, upload_to='files_pdf/', verbose_name='Файл PDF')),
                ('news_pdf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index_enbvu.news')),
            ],
        ),
    ]
