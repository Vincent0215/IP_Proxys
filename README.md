# IP_Proxys
get ip from internet with python<br>
用python3.6编辑实现，是自己写的第一个有功能的脚本。<br>
需求：<br>
从一个免费代理ip的网站获取该网站前几页的代理ip和相应的port，并保存到一个字典中以便使用。
使用python3.6实现。<br>
实现方法：<br>
1、百度查询‘免费代理ip’，从前几页中挑选一个比较正规简洁的免费ip网站，这里暂时选择 ‘https://www.kuaidaili.com/’<br>
2、分析前几页的网址规律，'https://www.kuaidaili.com/free/inha/1‘，'https://www.kuaidaili.com/free/inha/2‘，'https://www.kuaidaili.com/free/inha/3‘、
、、、、，所以只是最后一个字符代表页码，这个比较简单。<br>
3、用正则表达式提取里面的ip和port。<br>
4、将多页的结果保存在一起组成一个字典。<br>
