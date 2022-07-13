from django.db import models


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
        verbose_name_plural = '1. Обращение к руководителю (письма водопользователей)'
        ordering = ['-date_created']