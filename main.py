import urllib.request
import urllib.parse
import ssl
import re
import time

ip_group = []
port_group = []
ip_port_group = {}

def get_url():
    n = 1
    while n < 4 :
        url = 'https://www.kuaidaili.com/free/inha/%d' % n
        #print(url)
        get_html(url)
        n = n + 1
        time.sleep(3)
    print(ip_port_group)


def get_html(url):
    context = ssl._create_unverified_context()
    req = urllib.request.urlopen(url, timeout=10, context=context)
    html = req.read().decode('utf-8')
    #print(html)
    search_ip(html)

def search_ip(html):
    r_ip = re.compile(r'"IP">.+<')
    r_port = re.compile(r'"PORT">.+<')
    ip_group = r_ip.findall(html)
    port_group = r_port.findall(html)


    k = 0
    m = 0
    while k < len(ip_group):
        ip_group[k] = ip_group[k][5:-1]
        k = k + 1
    #print(ip_group)

    while m < len(port_group):
        port_group[m] = port_group[m][7:-1]
        m = m + 1
    #print(port_group)

    ip_port = dict(zip(ip_group, port_group))

    #print(ip_port)
    ip_port_group.update(ip_port)

    return ip_group, port_group


get_url()
