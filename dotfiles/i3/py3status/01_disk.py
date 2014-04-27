import subprocess


class Py3status:
    def disk(self, json, config):
        '''
            Get the disk usage for the root partition
        '''
        proc = subprocess.Popen(['df', '-h', '/'], stdout=subprocess.PIPE)
        disk = proc.communicate()[0].split('\n')[1].split()[3]
        return (
            0,
            {
                'name': 'disk',
                'full_text': '{: >4}'.format(disk),
                'color': '#ffffff',
            }
        )

    def on_click(self, json, conf, event):
        with open('/dev/null', 'w') as null:
            subprocess.Popen(
                ['/usr/bin/nautilus', '--no-desktop', '--new-window'],
                stdout=null,
                stderr=null,
            )
