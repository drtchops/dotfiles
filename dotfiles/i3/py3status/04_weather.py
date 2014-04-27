from subprocess import Popen
from time import time

from data_gc_ca_api import cityweather


class Py3status:
    CITY_NAME = 'Toronto'
    QUANTITY = 'currentConditions/temperature'
    CACHE_TIMEOUT = 1800

    def weather(self, json, config):
        temp = '?'
        timeout = 15

        try:
            index = cityweather.CityIndex()
            city = cityweather.City(index.data_url(self.CITY_NAME))
            temp = city.get_quantity(self.QUANTITY)
            timeout = self.CACHE_TIMEOUT
        except:
            pass

        return (
            0,
            {
                'name': 'weather',
                'instance': self.CITY_NAME,
                'full_text': u'{: >5}\xb0C'.format(temp),
                'color': '#ffffff',
                'cached_until': time() + timeout,
            }
        )

    def on_click(self, json, config, event):
        with open('/dev/null', 'w') as null:
            Popen(
                ['/usr/bin/xdg-open',
                 'http://weather.gc.ca/city/pages/on-143_metric_e.html'],
                stdout=null,
                stderr=null,
            )
