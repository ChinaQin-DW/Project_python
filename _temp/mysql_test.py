# -- coding:utf-8 --
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
yzm=driver.find_element_by_id("yznumber").text
print(yzm)
if yzm=='':
    print('None')
else:
    print('no')