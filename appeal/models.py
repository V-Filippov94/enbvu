from django.db import models
from enisey_bvu.models import ModePage, PictureFile


class AppealModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО отправителя')
    email = models.CharField(max_length=255, verbose_name='Email отправителя')
    address = models.TextField(verbose_name='Адрес', blank=True)
    message = models.TextField(verbose_name='Текст сообщения')
    file = models.FileField(upload_to='index_enbvu/obrashenie_files/', blank=True, verbose_name='Файл')
    get_approval = models.BooleanField(verbose_name='Согласие на обработку данных', blank=False)
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата отправления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = '2. Обращение к руководителю (письма водопользователей)'
        ordering = ['-date_created']


class UnMenuAppeal(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name[:103]


class ContentAppeal(models.Model):
    title = models.CharField(max_length=555, verbose_name='Заголовок', blank=True)
    content = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey(ModePage, on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_menu_appeal = models.ForeignKey('UnMenuAppeal', on_delete=models.CASCADE, verbose_name='Подпункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFileAppeal(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    content_appeal = models.ForeignKey('ContentAppeal', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FileAppeal(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='appeal/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFileAppeal', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    content_appeal = models.ForeignKey('ContentAppeal', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
