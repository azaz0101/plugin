# -*- coding:utf-8 -*-
import requests
import urllib
import sys
import os
from bs4 import BeautifulSoup

#搜尋條件
#print(sys.argv)
if len(sys.argv)>=3 and sys.argv[1]=='-q':
    search = sys.argv[2]
    # print(search)
    query = 'site:tfc-taiwan.org.tw/articles intitle:' + search
    URL = 'https://google.com/search?q='+query
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent":USER_AGENT}
    resp = requests.get(URL , headers = headers)
    text = resp.text.encode('utf8')

    #print(resp)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='r'):
            #print("hello")
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        #print(results)
        for msg in results:
            ans = msg['title'].split(u'】')[0]
            if(ans != u'【部分錯誤' and ans !=u'【錯誤'):
                continue
            print('<div id=title>'+msg['title']+'</div>')
            print('<a href="'+msg['link']+'">' +msg['link']+"</a>")
