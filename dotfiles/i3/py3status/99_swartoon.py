from subprocess import Popen
from random import choice


class Py3status:
    def swartoon(self, json, conf):
        return (
            0,
            {
                'full_text': 'fak u swartoon',
                'color': '#854191',
                'name': 'swartoon',
            },
        )

    def on_click(self, json, conf, event):
        with open('/dev/null', 'w') as null:
            f = choice(xrange(2, 5))
            Popen(
                ['/usr/bin/paplay', '/home/ian/Downloads/mu%s.aif' % f],
                stdout=null,
                stderr=null,
            )
