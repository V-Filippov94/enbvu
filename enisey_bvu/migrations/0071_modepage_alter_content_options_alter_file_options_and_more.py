# Generated by Django 4.0.5 on 2022-07-18 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index_enbvu', '0040_alter_mirvodyimage_options_alter_newsfilepdf_options_and_more'),
        ('enisey_bvu', '0070_content_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, verbose_name='Вид страницы')),
            ],
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Контент', 'verbose_name_plural': 'Добавить Контент'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Добавить файлы'},
        ),
        migrations.AlterField(
            model_name='content',
            name='unMenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_enbvu.unmenu', verbose_name='Подпункт меню'),
        ),
        migrations.AddField(
            model_name='content',
            name='mode_page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enisey_bvu.modepage', verbose_name='Вид страницы'),
            preserve_default=False,
        ),
    ]
