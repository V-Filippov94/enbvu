from django.db import models


class ModePage(models.Model):
    name = models.CharField(max_length=220, verbose_name='Вид страницы')

    def __str__(self):
        return self.name


class UnMenuENBVU(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name


class PictureFile(models.Model):
    name = models.CharField(max_length=255, verbose_name='Расширение файла')

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True)
    content = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey('ModePage', on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_menu_enbv = models.ForeignKey('UnMenuENBVU', on_delete=models.CASCADE, verbose_name='Подпункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFile(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:100]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class File(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='enisey_bvu/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFile', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey('PictureFile', on_delete=models.CASCADE, verbose_name='Расширение файла')
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить файлы'


