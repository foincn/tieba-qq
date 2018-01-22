#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: tools.py

import requests
from bs4 import BeautifulSoup

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


def get_page(href):
    for i in range(get_pn(href)):
        url = 'http://tieba.baidu.com/p/%s?pn=%s' % (href, i+1)
        print(url)
        r = s.get(url)
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


href_list = tieba_list(name, 10)
qq_list = []

for i in href_list:
    get_page(i)

cookie = ''

def get_cookies():
    result = {}
    cookies = cookie.split('; ')
    for i in cookies:
        key = i.split('=', 1)[0]
        value = i.split('=', 1)[1]
        result[key] = value
    return(result)

def qq_card(number):
number = '834539144'
url = 'http://ti.qq.com/cgi-bin/more_profile_card/more_profile_card'
payload = {'_q': number, 'bkn': '1527757257', 'src': 'mobile'}

