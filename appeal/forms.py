from django.forms import ModelForm, Textarea, TextInput, EmailInput, CheckboxInput
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import gettext_lazy
from captcha.fields import CaptchaField
from .models import AppealModel


class RequiredFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_required = getattr(self.Meta, 'fields_required', None)
        if fields_required:
            for key in self.fields:
                if key not in fields_required:
                    self.fields[key].required = False
                else:
                    self.fields[key].required = True


class AppealHead(RequiredFieldsMixin, ModelForm):
    captcha = CaptchaField(label='Введите текст капчи')

    class Meta:
        model = AppealModel
        fields = ['name', 'email', 'address', 'message', 'file', 'captcha', 'get_approval']
        fields_required = ['name', 'email', 'message', 'captcha', 'get_approval']
        labels = {
            'file': gettext_lazy('Прикрепить файл'),
            'get_approval': gettext_lazy(''),
        }
        help_texts = {
            'name': gettext_lazy('Заполнение является обязательным в соответствии с частью 3 статьи 7 Федерального '
                                 'закона от 2 мая 2006 г. № 59-ФЗ "О порядке рассмотрения обращений граждан Российской '
                                 'Федерации"',),

            'email': gettext_lazy( 'Заполнение является обязательным в соответствии с частью 3 статьи 7 Федерального '
                                   'закона от 2 мая 2006 г. № 59-ФЗ "О порядке рассмотрения обращений граждан '
                                   'Российской Федерации"'),

            'file': gettext_lazy('Поддерживаемые типы файлов: *.doc, *.docx, *.rar, *.pdf, *.jpg, *.tiff, *.png, *.xls,'
                                 ' *.xlsx, *.rtf, *.txt, *.zip, *.odt, *.ods Максимальный размер присоединяемого файла:'
                                 ' 10240 Кб.'),
        }

        widgets = {
            'name': TextInput(attrs={'placeholder': 'ФИО', 'class': 'name-user'}),
            'email': EmailInput(attrs={'placeholder': 'Email', 'class': 'email-user'}),
            'address': Textarea(attrs={'placeholder': 'Для ответа на обращение в письменной форме',
                                       'class': 'address-user', 'cols': '86'}),
            'message': Textarea(attrs={'placeholder': 'Добавьте сообщение', 'class': 'msg-user', 'cols': '86'}),
            'get_approval': CheckboxInput(attrs={'class': 'check-user'})
        }

