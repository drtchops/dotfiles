from subprocess import Popen, PIPE


class Py3status:
    def volume(self, json, config):
        pac = Popen(['pacmd', 'list-sinks'], stdout=PIPE)
        grep = Popen(['grep', '-A', '15', '* index'], stdin=pac.stdout, stdout=PIPE)
        awk = Popen(['awk', '/volume: front-left:/{print $5}'], stdin=grep.stdout, stdout=PIPE)
        vol = awk.communicate()[0].strip()

        pac = Popen(['pacmd', 'list-sinks'], stdout=PIPE)
        grep = Popen(['grep', '-A', '15', '* index'], stdin=pac.stdout, stdout=PIPE)
        awk = Popen(['awk', '/muted:/{print $2}'], stdin=grep.stdout, stdout=PIPE)
        muted = awk.communicate()[0].strip() == 'yes'

        return (
            -1,
            {
                'name': 'pulse',
                'instance': 'volume',
                'full_text': '{: >4}'.format(vol),
                'color': '#ff0000' if muted else '#ffffff',
            }
        )

    def on_click(self, json, config, event):
        with open('/dev/null', 'w') as null:
            Popen(
                ['/usr/bin/pactl', 'set-sink-mute', '1', 'toggle'],
                stdout=null,
                stderr=null,
            )
