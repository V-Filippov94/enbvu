from django.db import models
from enisey_bvu.models import PictureFile, ModePage


class UnMenuDeyatelnost(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')

    def __str__(self):
        return self.name[:103]


class ContentDeyatelnost(models.Model):
    title = models.CharField(max_length=555, verbose_name='Заголовок', blank=True)
    content = models.TextField(verbose_name='Текст страницы', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    mode_page = models.ForeignKey(ModePage, on_delete=models.CASCADE, verbose_name='Вид контекста')
    un_menu_deyatelnost = models.ForeignKey('UnMenuDeyatelnost', on_delete=models.CASCADE, verbose_name='Подпункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = '1. Добавить Контент'
        ordering = ['-date_change']


class ListFileDeyatelnost(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    content_deyatelnost = models.ForeignKey('ContentDeyatelnost', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FileDeyatelnost(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='deyatelnost/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFileDeyatelnost', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    content_deyatelnost = models.ForeignKey('ContentDeyatelnost', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        # verbose_name_plural = 'Добавить файлы'


class VodHoz(models.Model):
    sayno_sush = models.CharField(max_length=355, verbose_name='Саяно-Шушенское водохранилище')
    maiynskoe = models.CharField(max_length=355, verbose_name='Майнское водохранилище')
    kras = models.CharField(max_length=355, verbose_name='Красноярское водохранилище')
    irk = models.CharField(max_length=355, verbose_name='Иркутское водохранилище')
    bratsk = models.CharField(max_length=355, verbose_name='Братское водохранилище')
    ust_ilim = models.CharField(max_length=355, verbose_name='Усть-Илимское водохранилище')
    boguch = models.CharField(max_length=355, verbose_name='Богучанское водохранилище')
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return str(self.date_created)

    class Meta:
        verbose_name = 'Водохозяйственныую обстановку'
        verbose_name_plural = '2. Водохозяйственная обстановка'
        ordering = ['-date_created']


class Region(models.Model):
    name = models.CharField(max_length=355, verbose_name='Название региона')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регион'


class PrikazOZonePodtop(models.Model):
    district = models.CharField(max_length=255, verbose_name='Название района')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Регион')
    date_created = models.DateTimeField(verbose_name='Дата добавления')
    date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = 'Приказы об определении границы зоны затопления'
        verbose_name_plural = '3. Приказы об определении границы зоны затопления'


class ListFilePrikazOZonePodtop(models.Model):
    text = models.TextField(verbose_name='Текст (пояснение к файлу)', blank=True)
    prikaz_o_zone_podtop = models.ForeignKey('PrikazOZonePodtop', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:110]

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Добавить список файлов'


class FilePrikazOZonePodtop(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название файла', blank=True)
    file = models.FileField(upload_to='deyatelnost/prikazy_o_zone_podtop/files', blank=True, verbose_name='Файл')
    list_file = models.ForeignKey('ListFilePrikazOZonePodtop', on_delete=models.CASCADE, verbose_name='Пояснение к файлу')
    picture_file = models.ForeignKey(PictureFile, on_delete=models.CASCADE, verbose_name='Расширение файла')
    prikaz_o_zone_podtop = models.ForeignKey('PrikazOZonePodtop', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл'
        # verbose_name_plural = 'Добавить файлы'