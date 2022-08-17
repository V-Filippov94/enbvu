from django.db import models
from enisey_bvu.models import ModePage, PictureFile


class UnMenuCorruption(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name[:103]


class ContentCorruption(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True)
    content = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey(ModePage, on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_menu_corruption = models.ForeignKey('UnMenuCorruption', on_delete=models.CASCADE, verbose_name='Подпункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFileCorruption(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    content_corruption = models.ForeignKey('ContentCorruption', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FileCorruption(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='corruption/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFileCorruption', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    content_corruption = models.ForeignKey('ContentCorruption', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить файлы'


class AppealAntiCorruption(models.Model):
    title = models.CharField(max_length=250, verbose_name='Тема сообщения')
    text = models.TextField(verbose_name='Текст сообщения')
    file = models.FileField(upload_to='corruption/appeal_cor/files', blank=True, verbose_name='Прикрепленный файл')
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата отправки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Соощения о коррупции'
        verbose_name_plural = '2. Соощения о коррупции'
        ordering = ['-date_created']


class RatingWork(models.Model):
    high = models.BooleanField(verbose_name='Высокий уровень', default=False)
    average = models.BooleanField(verbose_name='Средний уровень', default=False)
    short = models.BooleanField(verbose_name='Низкий уровень', default=False)

