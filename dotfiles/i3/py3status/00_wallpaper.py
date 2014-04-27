from subprocess import Popen


class Py3status:
    def wallpaper(self, json, conf):
        return (0, {'full_text': 'WALL', 'name': 'wallpaper'})

    def on_click(self, json, conf, event):
        with open('/dev/null', 'w') as null:
            Popen(
                ['/home/ian/bin/random_wallpaper_x'],
                stdout=null,
                stderr=null,
            )
