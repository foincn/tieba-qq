#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: tools.py

import requests
from bs4 import BeautifulSoup
from ghost import
import re
import threading

s = requests.session()
s.keep_alive = False

name = '00后处对象'


def tieba_list(name, page):
    li = []
    for i in range(page):
        page_number = (i) * 50
        url = 'http://tieba.baidu.com/f?kw=%s&pn=%s' % (name, page_number)
        li += get_list(url)
    print(len(li))
    return(li)

def get_list(url):
    r = s.get(url)
    #r.status_code
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    #source = soup.select('#thread_list > li.j_thread_list.clearfix > div.t_con.cleafix > div.col2_right.j_threadlist_li_right > div.threadlist_lz.clearfix > div.threadlist_title.pull_left.j_th_tit > a')
    source = soup.select('#thread_list > li.j_thread_list')
    result = []
    for i in source:
        href = i.a.get('href').split('/')[2]
        result.append(href)
    return(result)



def get_pn(href):
    url = 'http://tieba.baidu.com/p/%s' % href
    r = s.get(url)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    pn = int(soup.select('span.red')[0].text)
    return pn


def get_page_url(href):
    for i in href_list: 
        for l in range(get_pn(href)):
            url = 'http://tieba.baidu.com/p/%s?pn=%s' % (href, l+1)
            url_list.append(url)


def get_page(url):
    print(url)
    r = None
    while r = None:
        try:
            r = s.get(url)
        expect:
            pass
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    source = soup.select('#j_p_postlist > div.l_post > div.d_post_content_main')
    for l in source:
        search_number(l.text)


def search_number(text):
    relink = '[0-9]{9,11}'
    p = re.compile(relink)
    li = p.findall(text)
    for i in li:
        qq_list.append(i)
    #return(result)


def login_qq():
    global se
    ua_m = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
    se = Session(Ghost(), user_agent=ua_m, wait_timeout=30, wait_callback=None, display=True, viewport_size=(375, 553), download_images=True)
    url = 'https://ui.ptlogin2.qq.com/cgi-bin/login?style=38&appid=728041403&s_url=https%3A%2F%2Finfoapp.3g.qq.com%2Fg%2Flogin%2Fproxy.jsp%3FsourceUrl%3Dhttps%25253A%25252F%25252Fportal.3g.qq.com%25252F%25253F_r%25253D0.2646472700205946%252526aid%25253Dindex%252526g_f%25253D1283&target=self&low_login=1&low_login_hour=4321&daid=261&islogin=false&uid=-8794356048489038000'
    se.open(url)
    se.set_field_value('#u', '2873723285')
    se.set_field_value('#p', 'tz1006')
    se.click('#go', expect_loading=True)


def check_qq(number):
    url = 'http://ti.qq.com/qcard/index.html?qq=%s' % number
    se.open(url)
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    age = soup.select('#age')[0].text
    gender = soup.select('#gender')[0].text
    if gender == '女':
        result.append(number)


href_list = tieba_list(name, 10)
url_list = []
qq_list = []
result = []


for i in href_list:
    get_page_url(i)



threads = []

for i in url_list:
    a = threading.Thread(target=get_page, args=(i,))
    threads.append(a)
    a.start()

for t in threads:
    t.join


login_qq()

for i in qq_list:
    if len(i) < 11:
        check_qq(i)
 
