import psutil
import shlex
import subprocess


def run_cmd(cmd):
    '''
        Run unix command in another process and return stdout
    '''
    cmd = shlex.split(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return proc.communicate()[0]


def read(path):
    '''
        Read the contents of a given file
    '''
    return open(path).read().strip()


class Py3status:
    def cpu(self, json, config):
        '''
            Get the cpu usage and temperature
        '''
        usage = int(round(psutil.cpu_percent()))
        temp = int(read('/sys/devices/platform/coretemp.0/temp1_input')) / 1000
        return (
            2,
            {
                'name': 'cpu',
                'full_text': u'%s%% %s\xb0C' % (usage, temp),
                'color': '#ff0000' if usage >= 75 or temp >= 75 else '#ffffff',
                'urgent': True if usage >= 75 or temp >= 75 else False,
            }
        )

    def memory(self, json, config):
        '''
            Get the virtual memory and swap usage
        '''
        ram = int(round(psutil.virtual_memory().percent))
        swap = int(round(psutil.swap_memory().percent))
        return (
            2,
            {
                'name': 'memory',
                'full_text': '%s%% %s%%' % (ram, swap),
                'color': '#ff0000' if ram >= 75 else '#ffffff',
                'urgent': True if ram >= 75 else False,
            }
        )

    def swartoon(self, json, conf):
        return (-1, {'full_text': 'fak u swartoon', 'color': '#854191', 'name': 'swartoon'})

    def wallpaper(self, json, conf):
        return (0, {'full_text': 'WALL', 'name': 'wallpaper'})

    def on_click(self, json, conf, event):
        with open('/home/ian/t', 'a') as t:
            t.write(str(event))
            t.wrtie('\n')
        if event['name'] == 'wallpaper':
            run_cmd('random_wallpaper_x')


# #!/usr/bin/env python

# from __future__ import print_function
# import datetime
# import psutil
# import shlex
# import netifaces
# import subprocess
# import time
# import ujson


# def _run_cmd(cmd):
#     '''Run unix command'''
#     cmd = shlex.split(cmd)
#     proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
#     return proc.communicate()[0]


# def _read(path):
#     '''Get contents of file'''
#     return open(path).read().strip()


# if __name__ == '__main__':
#     # Send the header so that i3bar knows we want to use JSON:
#     print('{"version":1}')
#     # Begin the endless array.
#     print('[')
#     # We send an empty first array of blocks to make the loop simpler:
#     # print('[],')

#     # run forever
#     while True:
#         # get disk usage
#         try:
#             disk = _run_cmd('df -h /').split('\n')[1].split()[3]
#         except:
#             disk = '?'

#         # get ram usage
#         try:
#             ram = int(round(psutil.virtual_memory().percent))
#         except:
#             ram = '?'

#         # get swap usage
#         try:
#             swap = int(round(psutil.swap_memory().percent))
#         except:
#             swap = '?'

#         # get cpu usage
#         try:
#             cpu = int(round(psutil.cpu_percent()))
#         except:
#             cpu = '?'

#         # get ip addr
#         try:
#             ip = netifaces.ifaddresses('eth0')[2][0]['addr']
#         except:
#             ip = '?'

#         # get battery status
#         try:
#             bats = _read('/sys/class/power_supply/BAT0/status')
#             batc = int(_read('/sys/class/power_supply/BAT0/capacity'))
#         except:
#             bats = '?'
#             batc = '?'

#         # get current time
#         try:
#             sdate = datetime.datetime.now().strftime('%a %b %d, %Y %I:%M %p').replace(' 0', ' ')
#             stime = datetime.datetime.now().strftime('%I:%M %p').replace(' 0', ' ')
#         except:
#             date = '?'

#         # format for i3bar
#         out = [{
#             'name': 'disk',
#             'full_text': '/: %s' % disk,
#             'min_width': '/: 100G',
#             'color': '#ffffff',
#         }, {
#             'name': 'memory',
#             'instance': 'ram',
#             'full_text': 'RAM: %s%%' % ram,
#             'min_width': 'RAM: 100%',
#             'color': '#ff0000' if ram >= 90 else '#ffffff',
#             'urgent': True if ram >= 90 else False,
#         }, {
#             'name': 'memory',
#             'instance': 'swap',
#             'full_text': 'Swap: %s%%' % swap,
#             'min_width': 'Swap: 100%',
#             'color': '#ff0000' if swap >= 50 else '#ffffff',
#             'urgent': True if swap >= 50 else False,
#         }, {
#             'name': 'cpu',
#             'full_text': 'CPU: %s%%' % cpu,
#             'min_width': 'CPU: 100%',
#             'color': '#ff0000' if cpu >= 75 else '#ffffff',
#             'urgent': True if cpu >= 75 else False,
#         }, {
#             'name': 'ethernet',
#             'instance': 'eth0',
#             'full_text': 'IP: %s' % ip,
#             'color': '#ffffff',
#         }, {
#             'name': 'bat',
#             'full_text': 'Bat: %s %s%%' % (bats, batc),
#             'color': '#ff0000' if batc <= 30 else '#ffffff',
#             'urgent': True if batc <= 30 else False,
#         }, {
#             'name': 'date',
#             'full_text': sdate,
#             'short_text': stime,
#             'color': '#ffffff',
#         }]

#         # json for i3bar
#         print(ujson.dumps(out) + ',')

#         # Update interval in seconds
#         time.sleep(2)
