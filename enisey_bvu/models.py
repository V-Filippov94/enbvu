from django.db import models


class FunctionUprav(models.Model):
    text_function = models.TextField(verbose_name='Основные функции Управления')

    def __str__(self):
        return self.text_function

    class Meta:
        verbose_name = 'Основную функцию Управления'
        verbose_name_plural = '1.  Основные функции Управления  "(Функции и полномочия Енисейского БВУ)"'
        ordering = ['id']


class Polnomochiya(models.Model):
    text_polnomochiya = models.TextField(verbose_name='Полномочия')

    def __str__(self):
        return self.text_polnomochiya

    class Meta:
        verbose_name = 'Пункт полномочий'
        verbose_name_plural = '1.1  Полномочия "(Функции и полномочия Енисейского БВУ)"'
        ordering = ['id']


class NormAktFunction(models.Model):
    title = models.TextField(verbose_name='Название документа')
    file_pdf = models.FileField(upload_to='enisey_bvu/normativnye_akty_function', verbose_name='Документ', blank=True)
    date_created = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = '2. Нормативные акты, определяющие полномочия, задачи и функции'
        ordering = ['id']


class Organization(models.Model):
    name = models.CharField(max_length=300, verbose_name='Наименование организации')
    address = models.TextField(verbose_name='Адрес')
    address_cor = models.TextField(verbose_name='Адрес для корреспонденции', blank=True)
    mode = models.CharField(max_length=300, verbose_name='Режим работы', blank=True)
    fax = models.CharField(max_length=20, verbose_name='Факс', blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организацию'
        verbose_name_plural = '3.1 Организация ("Структура управления")'


class PhoneOrganization(models.Model):
    number = models.CharField(max_length=20, verbose_name='Телефон организации')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефоны организации'
        verbose_name_plural = 'Телефон организации'


class SectorOrganization(models.Model):
    name = models.CharField(max_length=355, verbose_name='Отдел')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО сотрудника')
    post = models.CharField(max_length=255, verbose_name='Должность')
    email = models.CharField(max_length=255, verbose_name='Email')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name='Организация')
    sector_organization = models.ForeignKey('SectorOrganization', on_delete=models.CASCADE, verbose_name='Отдел')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = '3.2 Сотрудники ("Структура управления")'


class PhoneWorker(models.Model):
    number = models.CharField(max_length=20, verbose_name='Телефон сотрудника')
    worker = models.ForeignKey('Worker', on_delete=models.CASCADE)

    def __str__(self):
        return 'Номер'

    class Meta:
        verbose_name = 'Телефон сотрудника'
        verbose_name_plural = 'Телефоны сотрудника'


class Uchrezhdeniya(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название учреждения')
    worker_name = models.CharField(max_length=255, verbose_name='ФИО руководителя')
    post = models.CharField(max_length=255, verbose_name='Должность')
    site = models.CharField(max_length=255, verbose_name='Сайт', blank=True)
    email = models.CharField(max_length=255, verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подведомственное учреждение'
        verbose_name_plural = '4. Подведомственные учреждения'


class AddressUchrezhdeniya(models.Model):
    address = models.TextField(verbose_name='Адрес Подведомственного учреждения')
    uchrezhdenie = models.ForeignKey('Uchrezhdeniya', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес Подведомственного учреждения'
        verbose_name_plural = 'Адрес Подведомственного учреждения'


class PhoneUchrezhdeniya(models.Model):
    phone = models.CharField(max_length=255, verbose_name='Телефон Подведомственного учреждения')
    uchrezhdenie = models.ForeignKey('Uchrezhdeniya', on_delete=models.CASCADE)
    address = models.ForeignKey('AddressUchrezhdeniya', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Телефон Подведомственного учреждения'
        verbose_name_plural = 'Телефоны Подведомственного учреждения'


class InfoZakupki(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст статьи')
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью закупки'
        verbose_name_plural = '5. Информация об осуществлении закупок товаров, работ, услуг для государственных нужд'


class PlanProverok(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'План проверок'
        verbose_name_plural = '6. План проверок, результаты проверок'
        ordering = ['id']


class OficialVystup(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    file_pdf = models.FileField(upload_to='enisey_enbvu/oficial-vystupleniya_pdf', verbose_name='Файл пдф', blank=True)
    date_created = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Официальное выступление или заявление'
        verbose_name_plural = '7.  Официальные выступления и заявления'


class SvedeniyaSmi(models.Model):
    text = models.TextField(verbose_name='Текст')
    date_created = models.DateTimeField(verbose_name='Дата добавления')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сведения о финансировании (отсутсвии финансирования) средств массовой информации'
        verbose_name_plural = '8.  Сведения о финансировании (отсутсвии финансирования) средств массовой информации'
















