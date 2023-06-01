# 先导入模块os，用于文件操作
import os
import urllib.request

import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'
}
params = {
    'Referer' :'https://www.itingwa.com/'
}
cookies = {'Cookie': 'h=zVbrujM86zc6DrNphgelLw; e=1685105822; Hm_lvt_c37219ae99edc71b0fb7d4cb8b094498=1685104008; Hm_lpvt_c37219ae99edc71b0fb7d4cb8b094498=1685105195; __utma=158286818.94899063.1685104008.1685104008.1685104008.1; __utmb=158286818.8.10.1685104008; __utmc=158286818; __utmz=158286818.1685104008.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1'}
playurl = 'https://tingwa.oss-cn-shanghai.aliyuncs.com/2020-04/10/20200410121136-ODUyMDM3.mp3?OSSAccessKeyId=3b1nzo7roav1h50rcp0a35nw&Expires=1685106167&Signature=kpCmAXBtjDkbS2iGeu2M4PwJH94='

# 这个意思就是如果当前路径没有这个文件夹，就创建这个文件夹，方便把我们的音乐文件放在这里
if not os.path.exists('./music/'):
    os.mkdir('./music/')
# content方法就是获取网址的二进制数据
content = requests.get(url=playurl, headers=headers,cookies=cookies,params=params).content
# 打开文件，并在文件里写入二进制数据
with open('./music/{name} {singer}.mp3'.format(name='初夏的风', singer='hee2t'), 'wb') as f:
    f.write(content)
    f.close()
print('下载完成')
