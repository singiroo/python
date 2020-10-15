import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button1Function)
        
        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        #http://localhost/HelloWeb/hello.jsp
        #https://map.naver.com/v5/search/%EB%A7%9B%EC%A7%91/place/16069633?c=14184560.2696510,4345479.6935407,16,0,0,0,dh
        #https://place.map.kakao.com/12468740
        self.browser.get("https://place.map.kakao.com/12468740")

    def button1Function(self) :
        objs = self.browser.find_element_by_class_name("list_menu").find_elements_by_tag_name("li")
        for obj in objs:
            print(obj.text.split("\n"))


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
