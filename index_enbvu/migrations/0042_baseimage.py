# Generated by Django 4.0.5 on 2022-08-10 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0041_remove_newsfiles_news_file_delete_newsfilepdf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='index_enbvu/news/image_news/', verbose_name='Фото')),
                ('css', models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс')),
            ],
        ),
    ]