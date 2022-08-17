from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    url = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = '1. Меню'
        ordering = ['id']


class UnMenu(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    url = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Menu', on_delete=models.PROTECT, verbose_name='Пункт меню')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню ПодПункт'
        verbose_name_plural = '2. Меню ПодПункты'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='Текст Новости')
    hot = models.BooleanField(verbose_name='Горячая новость', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = '1. Новости'
        ordering = ['-date_create']


class NewsImage(models.Model):
    image = models.ImageField(upload_to='index_enbvu/news/image_news/', blank=True, verbose_name='Фото')
    news = models.ForeignKey('News', on_delete=models.CASCADE, verbose_name='Новость')
    css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return 'Фото'

    class Meta:
        verbose_name = 'Фото, картинки'
        verbose_name_plural = 'Добавить Фото'


class PhotoLink(models.Model):
    photo = models.ImageField(upload_to='index_enbvu/photo_link', verbose_name='Картинка')
    url = models.CharField(max_length=300, verbose_name='Ссылка на ресурс')

    class Meta:
        verbose_name = 'Ссылку на внешний ресурс'
        verbose_name_plural = '2. Ссылки на внешний ресурс'


class VeteranList(models.Model):
    photo = models.ImageField(upload_to='index_enbvu/photo_veteran', verbose_name='Фото')
    date_created = models.DateTimeField(verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Фото ветерана'
        verbose_name_plural = '4. Бессмертный полк'


class MirVodyYear(models.Model):
    slug = models.SlugField(max_length=200, verbose_name='Год конкурса')
    date_created = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('mir_vody', kwargs={'mir_vody_slug': self.slug})

    class Meta:
        verbose_name = 'Год конкурса'
        verbose_name_plural = '3. Мир воды'


class MirVodyImage(models.Model):
    image = models.ImageField(upload_to='index_enbvu/mir_vody/', blank=True, verbose_name='Фото')
    mir_vody_year = models.ForeignKey('MirVodyYear', on_delete=models.CASCADE, verbose_name='Рисунок')

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Фото, картинки'
        verbose_name_plural = 'Добавить Фото'

