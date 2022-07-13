from .models import *
import requests


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

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = Menu.objects.all()
        context['un_menu'] = UnMenu.objects.all()
        context['photo_link'] = PhotoLink.objects.all()
        context['info_weather'] = self.city_info
        print(self.city_info)
        return context
