# -- coding:utf-8 --

#elements = driver.find_elements_by_class_name("STYLE1")
#elements[11].click()  #第11个元素为点击登录按钮

from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
kh_01='2019'
kh_02=48## start 001 - 299
kh_03='00'#00 01 02
kh_04='263'
xm='高明'
def cjcx(kh,xm):
    driver.find_element_by_id("number").clear()
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("number").send_keys(kh)#考号
    driver.find_element_by_id("name").send_keys(xm)#名字
    driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
    tit=(driver.title)
    time.sleep(0.1)
    print(kh+xm)
    if tit=='成绩查询':
        return tit
    driver.find_element_by_id("button").click()  # 上一步

time.sleep(5)  #等待输入验证码
for n in range(0,5):
    kh_03='0'+str(n)
    for n in range(190,300):
        if n<10:
            m='00'+str(n)
        elif n<100:
            m = '0' + str(n)
        elif n<1000:
            m = str(n)
        kh=kh_01+m+kh_03+kh_04
        tit=cjcx(kh,xm)
        if tit=='成绩查询':
            break
    if tit == '成绩查询':
        print('查到成绩')
        break
##cjcx('201908200295','熊晓辉')
##成绩查询




