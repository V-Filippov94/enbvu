from django.db import models
from enisey_bvu.models import ModePage, PictureFile


class UnMenuOkazanieGosuslug(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name[:103]


class ContentOkazanieGosuslug(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True)
    content_okazanie_gosuslug = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey(ModePage, on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_menu_okazanie_gosuslug = models.ForeignKey('UnMenuOkazanieGosuslug', on_delete=models.CASCADE,
                                                  verbose_name='Подпункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFileOkazanieGosuslug(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    content_okazanie_gosuslug = models.ForeignKey('ContentOkazanieGosuslug', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FileOkazanieGosuslug(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='okazanie_gosuslug/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFileOkazanieGosuslug', on_delete=models.CASCADE,
                                  verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    content_okazanie_gosuslug = models.ForeignKey('ContentOkazanieGosuslug', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить файлы'
