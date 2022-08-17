from django.db.models import Max
import requests
from .models import *

from appeal.models import *
from corruption.models import *
from deyatelnost.models import *
from enisey_bvu.models import *
from kadr_provision.models import *
from normativ_document.models import *
from okazanie_gosuslug.models import *


class DataMixin:
    appid = 'a8d515f5b5414ccee8c75ed31552f521'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Krasnoyarsk'
    res = requests.get(url.format(city)).json()
    temp = str(res['main']['temp'])

    city_info = {
        'city': city,
        'temp': temp[:2],
        'icon': res['weather'][0]['icon'],
    }

    def get_user_context(self, unMenuArg=None, unMenuNormAkt=None, unMenuDeyatelnost=None, unPageKadr=None,
                         unMenuOkazanieGosuslug=None, unMenuAppeal=None, unMenuCorrution=None, **kwargs):
        context = kwargs
        context['menu'] = Menu.objects.all()
        context['un_menu'] = UnMenu.objects.all()
        context['photo_link'] = PhotoLink.objects.all()
        context['info_weather'] = self.city_info

        context['obj_model'] = Content.objects.filter(un_menu_enbv=unMenuArg)
        context['list_files'] = ListFile.objects.all().order_by('-id')
        context['files'] = File.objects.all()
        context['date_created'] = Content.objects.filter(un_menu_enbv=unMenuArg).first()
        context['date_change'] = Content.objects.filter(un_menu_enbv=unMenuArg).aggregate(Max('date_change'))
        context['picture_file'] = PictureFile.objects.all()

        context['obj_model_norm_akt'] = ContentNormAkt.objects.filter(un_menu_norm_akt=unMenuNormAkt)
        context['list_files_norm_akt'] = ListFileNormAkt.objects.all().order_by('-id')
        context['files_norm_akt'] = FileNormAkt.objects.all()
        context['date_created_norm_akt'] = ContentNormAkt.objects.filter(un_menu_norm_akt=unMenuNormAkt).first()
        context['date_change_norm_akt'] = ContentNormAkt.objects.filter(un_menu_norm_akt=unMenuNormAkt).aggregate(
            Max('date_change'))

        context['obj_model_deyatelnost'] = ContentDeyatelnost.objects.filter(un_menu_deyatelnost=unMenuDeyatelnost)
        context['list_files_deyatelnost'] = ListFileDeyatelnost.objects.all().order_by('-id')
        context['files_deyatelnost'] = FileDeyatelnost.objects.all()
        context['date_created_deyatelnost'] = ContentDeyatelnost.objects.filter(
            un_menu_deyatelnost=unMenuDeyatelnost).first()
        context['date_change_deyatelnost'] = ContentDeyatelnost.objects.filter(
            un_menu_deyatelnost=unMenuDeyatelnost).aggregate(Max('date_change'))

        context['obj_model_kadr'] = KadrProvision.objects.filter(un_page=unPageKadr)
        context['list_files_kadr'] = ListFileKadr.objects.all().order_by('-id')
        context['files_kadr'] = FileKadr.objects.all()
        context['date_created_kadr'] = KadrProvision.objects.filter(un_page=unPageKadr).first()
        context['date_change_kadr'] = KadrProvision.objects.filter(un_page=unPageKadr).aggregate(
            Max('date_change'))

        context['obj_model_okazanie_gosuslug'] = ContentOkazanieGosuslug.objects.filter(
            un_menu_okazanie_gosuslug=unMenuOkazanieGosuslug)
        context['list_files_okazanie_gosuslug'] = ListFileOkazanieGosuslug.objects.all().order_by('-id')
        context['files_okazanie_gosuslug'] = FileOkazanieGosuslug.objects.all()
        context['date_created_okazanie_gosuslug'] = ContentOkazanieGosuslug.objects.filter(
            un_menu_okazanie_gosuslug=unMenuOkazanieGosuslug).first()
        context['date_change_okazanie_gosuslug'] = ContentOkazanieGosuslug.objects.filter(
            un_menu_okazanie_gosuslug=unMenuOkazanieGosuslug).aggregate(
            Max('date_change'))

        context['obj_model_appeal'] = ContentAppeal.objects.filter(un_menu_appeal=unMenuAppeal)
        context['list_files_appeal'] = ListFileAppeal.objects.all().order_by('-id')
        context['files_appeal'] = FileAppeal.objects.all()
        context['date_created_appeal'] = ContentAppeal.objects.filter(un_menu_appeal=unMenuAppeal).first()
        context['date_change_appeal'] = ContentAppeal.objects.filter(un_menu_appeal=unMenuAppeal).aggregate(
            Max('date_change'))

        context['obj_model_corruption'] = ContentCorruption.objects.filter(un_menu_corruption=unMenuCorrution)
        print(context['obj_model_corruption'])
        context['list_files_corruption'] = ListFileCorruption.objects.all().order_by('-id')
        context['files_corruption'] = FileCorruption.objects.all()
        context['date_created_corruption'] = ContentCorruption.objects.filter(
            un_menu_corruption=unMenuCorrution).first()
        context['date_change_corruption'] = ContentCorruption.objects.filter(
            un_menu_corruption=unMenuCorrution).aggregate(Max('date_change'))
        return context
