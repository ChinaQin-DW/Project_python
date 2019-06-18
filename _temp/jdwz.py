# -- coding:utf-8 --
#elements = driver.find_elements_by_class_name("STYLE1")
#elements[11].click()  #第11个元素为点击登录按钮

from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
kh_01='2019'
kh_02=48## start 001 - 299
kh_03='02'#00 01 02
kh_04='287'
xm='文晶晶'
def cjcx(kh,xm):
    driver.find_element_by_id("number").clear()
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("number").send_keys(kh)#考号
    driver.find_element_by_id("name").send_keys(xm)#名字
    driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
    print(driver.title)
    time.sleep(1)
    print(kh+xm)
    driver.find_element_by_id("button").click()  # 上一步

time.sleep(5)  #等待输入验证码
for n in range(82,300):
    if n<100:
        m='0'+str(n)
    else:
        m=str(n)
    kh=kh_01+m+kh_03+kh_04
    cjcx(kh,xm)




