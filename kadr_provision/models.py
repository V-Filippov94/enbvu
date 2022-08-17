from django.db import models
from enisey_bvu.models import PictureFile, ModePage


class UnPageKadr(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name


class KadrProvision(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True)
    content_kadr = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey(ModePage, on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_page = models.ForeignKey('UnPageKadr', on_delete=models.CASCADE, verbose_name='Выбор страницы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFileKadr(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    kadr_provision = models.ForeignKey('KadrProvision', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FileKadr(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='deyatelnost/kadry/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFileKadr', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    kadr_provision = models.ForeignKey('KadrProvision', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'

