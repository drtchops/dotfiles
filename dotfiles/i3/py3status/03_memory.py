import psutil
from subprocess import Popen


class Py3status:
    def memory(self, json, config):
        '''
            Get the virtual memory and swap usage
        '''
        ram = int(round(psutil.virtual_memory().percent))
        swap = int(round(psutil.swap_memory().percent))
        return (
            0,
            {
                'name': 'memory',
                'full_text': '{: >4}% {: >4}%'.format(ram, swap),
                'color': '#ff0000' if ram >= 75 else '#ffffff',
                'urgent': True if ram >= 75 else False,
            }
        )

    def on_click(self, json, conf, event):
        with open('/dev/null', 'w') as null:
            Popen(
                ['/usr/bin/urxvt', '-e', 'htop'],
                stdout=null,
                stderr=null,
            )
