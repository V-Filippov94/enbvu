# Generated by Django 4.0.4 on 2022-07-03 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0036_alter_newsfilepdf_pdf_alter_newsfiles_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirvodyimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='index_enbvu/mir_vody/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='mirvodyimage',
            name='mir_vody_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.mirvodyyear', verbose_name='Рисунок'),
        ),
        migrations.AlterField(
            model_name='newsfilepdf',
            name='news_pdf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.news'),
        ),
        migrations.AlterField(
            model_name='newsfiles',
            name='news_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.news'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.news', verbose_name='Новость'),
        ),
    ]
