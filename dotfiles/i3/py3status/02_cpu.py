import psutil
from subprocess import Popen


class Py3status:
    def cpu(self, json, config):
        '''
            Get the cpu usage and temperature
        '''
        usage = int(round(psutil.cpu_percent()))
        temp = int(open('/sys/devices/platform/coretemp.0/temp1_input').read().strip()) / 1000
        return (
            0,
            {
                'name': 'cpu',
                'full_text': u'{: >4}% {: >3}\xb0C'.format(usage, temp),
                'color': '#ff0000' if usage >= 75 or temp >= 75 else '#ffffff',
                'urgent': True if usage >= 75 or temp >= 75 else False,
            }
        )

    def on_click(self, json, conf, event):
        with open('/dev/null', 'w') as null:
            Popen(
                ['/usr/bin/urxvt', '-e', 'htop'],
                stdout=null,
                stderr=null,
            )
