## chrome version 86.0.4240.75

from selenium import webdriver as wd
driver = wd.Chrome(executable_path="chromedriver.exe") 
url = "https://www.naver.com" 
driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")



