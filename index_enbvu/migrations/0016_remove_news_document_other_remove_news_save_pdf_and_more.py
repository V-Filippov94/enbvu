# Generated by Django 4.0.5 on 2022-06-22 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0015_alter_newsimage_image_newsfiles_newsfilepdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='document_other',
        ),
        migrations.RemoveField(
            model_name='news',
            name='save_pdf',
        ),
        migrations.AddField(
            model_name='news',
            name='files',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='index_enbvu.newsfiles'),
            preserve_default=False,
        ),
    ]