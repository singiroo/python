# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import time
import requests
import sqlite3
from bs4 import BeautifulSoup



## VO클래스
class CrawlingVo():
    title=""
    link=""
    category=""
    description=""
    telephone=""
    address=""
    roadAddress=""
    map_x=""
    map_y=""
    
    def __init__(self):
        pass



## 네이버 open API를 활용하여 정보 받아오기        
class getOpenApi():
    
    def __init__(self):
        self.client_id = "c2B6tQ6F7XTAKp6g8sny"
        self.client_secret = "uBROrFUpwH"
        self.encText = urllib.parse.quote("대전 대흥동 맛집")
        self.url = "https://openapi.naver.com/v1/search/local.xml?query=" + self.encText + "&display=5" # json 결과
    
    def submit(self):
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        
        if(rescode==200):
            response_body = response.read()
            
            response_decode = response_body.decode('utf-8')
            print(response_decode);
            
            return response_decode
            
        #     print(response_decode)
        else:
            return "Error Code:" + rescode
    


## HTTP GET Request
## HTML 소스 가져오기
class Parser():
    
    def __init__(self):
        self.naver = getOpenApi()
        self.result = self.naver.submit()
## BeautifulSoup으로 html소스를 python객체로 변환하기
## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
## 이 글에서는 Python 내장 html.parser를 이용했다.
        self.soup = BeautifulSoup(self.result, 'xml')
        self.my_titles = self.soup.find_all('item')
#         for v in self.my_titles:
#             print(v)
    ## my_titles는 list 객체
    
    def setVoList(self):   
        voList = []
        for item in self.my_titles:
            ## Tag안의 텍스트
            vo = CrawlingVo();
            vo.title = item.title.text;
            vo.link = item.link.text;
            vo.category = item.category.text;
            vo.description = item.description.text;
            vo.telephone = item.telephone.text;
            vo.address = item.address.text;
            vo.roadAddress = item.roadAddress.text;
            vo.map_x = item.mapx.text;
            vo.map_y = item.mapy.text;
            voList.append(vo)
 
        return voList


## db에 저장

parser = Parser()
list = parser.setVoList()
conn = sqlite3.connect("crawlingdb.db", isolation_level=None)
  
cursor = conn.cursor()
sql = "insert into crawling values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
  
for i in range(len(list)):
    data = (list[i].title, list[i].link, list[i].category,
            list[i].description, list[i].telephone, list[i].address,
            list[i].roadAddress, list[i].map_x, list[i].map_y)
    cursor.execute(sql,data)
  
#conn.commit()
  
conn.close()






    
