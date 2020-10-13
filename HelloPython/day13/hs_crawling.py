#제목: 네이버 검색 API 활용하기
 
#import
import os
import sys
import time
import urllib.request
import requests
from bs4 import BeautifulSoup


 
#애플리케이션 클라이언트 id 및 secret
client_id = "vSrhWEauWM31KSkRgmnJ" 
client_secret = "zeSv_5apNi"

encText = urllib.parse.quote("대전 대흥동 맛집")
displayLine = "&display=5"
# url = "https://openapi.naver.com/v1/search/blog?query=" + query # json 결과
url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText + displayLine # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()


if(rescode==200):
    response_body = response.read()
            
    response_decode = response_body.decode('utf-8')

    print(response_decode)
    
    
    soup = BeautifulSoup(response_decode, 'html.parser')
    print(soup)
    
    items = soup
#     print(items)
    for item in items:
        pass
        
         
#         title = item.find("title").text
#         link = item.find_next().find_next().text
#         category = item.find("category").text
#         description = item.find("description").text
#         telephone = item.find("telephone").text
#         address = item.find("address").text
#         roadaddress = item.find("roadaddress").text
#         mapx = item.find("mapx").text
#         mapy = item.find("mapy").text
#          
#          
#         print("title : ", title)
#         print("link : ", link)
#         print("category : ", category)
#         print("description : ", description)
#         print("telephone : ", telephone)
#         print("address : ", address)
#         print("roadaddress : ", roadaddress)
#         print("mapx : ", mapx)
#         print("mapy : ", mapy)
    
else:
    print("Error Code:" + rescode)


# print(soup)
my_titles = soup.select(
    'item'
    )

for it in my_titles:
    print(it.title.text)

