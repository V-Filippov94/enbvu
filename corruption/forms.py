from django.forms import ModelForm, TextInput, Textarea, RadioSelect, ChoiceField
from django.utils.translation import gettext_lazy
from captcha.fields import CaptchaField

from .models import AppealAntiCorruption


class AppealAniCor(ModelForm):
    captcha = CaptchaField(label='Введите текст каптчи')

    class Meta:
        model = AppealAntiCorruption
        fields = ['title', 'text', 'file', 'captcha']
        labels = {
            'file': gettext_lazy('Прикрепить файл'),
        }
        help_texts = {
            'file': 'Поддерживаемые типы файлов: *.doc, *.docx, *.rar, *.pdf, *.jpg, *.tiff, *.png, *.xls, *.xlsx, '
                    '*.rtf, *.txt, *.zip, *.odt, *.ods Максимальный размер присоединяемого файла: 10240 Кб.'
        }
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Тема', 'class': 'name-user'}),
            'text': Textarea(attrs={'placeholder': 'Добавьте сообщение', 'class': 'msg-user', 'cols': '86'})
        }

