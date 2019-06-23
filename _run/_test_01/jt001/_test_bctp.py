# -- coding:utf-8 --
from selenium import webdriver
import time
import pytesseract
from PIL import Image

#打开浏览器
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
time.sleep(1)
element=driver.find_element_by_xpath("//img[contains(@src, '/2019cjfb/register/image.jsp')]")
element.screenshot('yzm_1.png')
img = Image.open('yzm_1.png')  # 根据地址，读取图片
code = pytesseract.image_to_string(img)  # 读取里面的内容
print(code)
driver.find_element_by_id("number").send_keys('2222')#考号
driver.find_element_by_id("name").send_keys('啊啊啊')#名字
driver.find_element_by_id("yznumber").send_keys(code)#
driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
time.sleep(1)
zfc=driver.find_element_by_xpath("//span[contains(@style, 'font-size:16px; font-weight:bold; color:#FF0000')]")
##您访问系统过于频繁，请30分钟后登录系统进行查询！
print(zfc.text)
driver.close()
time.sleep(1)
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')