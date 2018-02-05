import urllib.request
import urllib.parse
import ssl
import re
import time

ip_group = [] #一个暂时存ip地址的元组，单次存一个网页内的内容
port_group = [] #一个暂存port值的元组，单次存一个网页内的内容
ip_port_group = {} #存储最终ip与port组合的字典，也就是最终要得到的输出结果

def get_url():
    n = 1
    while n <= 4 :  # n代表要抓取的页数，个人建议一般只要抓取前几页，过后的数据比较旧，也不太有用
        url = 'https://www.kuaidaili.com/free/inha/%d' % n  #示例的网址，后期如果更改网址，需要更改此处，n代表网页页码，可能其它网页的表示方法不一样，需要做相应的修改。
        #print(url)
        get_html(url)
        n = n + 1
        time.sleep(3) #每抓取一次，暂停3秒，防止抓取过快被禁止访问
    print(ip_port_group)


def get_html(url):
    context = ssl._create_unverified_context()  #因为之前访问时出现提示ssl错误（应该是证书不受信任），不明白什么意思，后上网搜索后只要加上这段代码就可以了。
    req = urllib.request.urlopen(url, timeout=10, context=context)  # 打开网址，附上访问超时为10s，但此处可能要再加一个访问超时的错误的错误异常抛出，后期再改（如果有必要）。
    html = req.read().decode('utf-8') #读取网页内容
    #print(html)
    search_ip(html)

def search_ip(html):
    r_ip = re.compile(r'"IP">.+<')  #设定搜索条件，在打开网页源码后发现源码中的ip地址都以这样的格式存储：<td data-title="IP">117.90.3.114</td> <td data-title="PORT">9000</td>。
    r_port = re.compile(r'"PORT">.+<')
    ip_group = r_ip.findall(html) #将搜索出来的结果，暂存在ip_group中，此时存储的样式为："IP">117.90.3.114< ，后面会将数据过虑一次
    port_group = r_port.findall(html)  #将搜索出来的结果，暂存在port_group中，此时存储的样式为："PORT">9000< ，后面会将数据过虑一次

# 以下为将数据过滤一次，重新储存到原元组中。将数据的头 '"IP">' ，尾 '<' ,去掉。只留下‘117.90.3.114’。port_group与ip_group相同的操作。
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

    ip_port = dict(zip(ip_group, port_group))  # 将ip_group与port_group组合成一个临时字典存储到 ip_port中。

    #print(ip_port)
    ip_port_group.update(ip_port) # 将ip_port添加到ip_port_group中，因为ip_port只是临时存储单个网页的ip数据，最终每一页要汇总到ip_port_group中。

    return ip_group, port_group


get_url()
