# -- coding:utf-8 --
import csv
from selenium import webdriver
import time

#打开浏览器
driver=webdriver.Firefox()
driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
# 等待首次输入验证码
time.sleep(10)
#定义查询函数
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
    elif tit=='军队文职人员招考网报':
        driver.find_element_by_id("button").click()  # 上一步

def int_str(intkch):
    if intkch < 10:
        kh_2 = '00' + str(intkch)
    elif intkch < 100:
        kh_2 = '0' + str(intkch)
    elif intkch < 1000:
        kh_2 = str(intkch)
    return kh_2
gwdm_0=''
kc_0=1
#打开csv源
with open("a1_in.csv","r",encoding='UTF-8') as csvfile:
    cf = csv.reader(csvfile)
    for aa in cf:
        xx_list=aa
        kh_4=aa[0][-3:]
        xm=aa[1]
        gwdm=aa[2]
        if gwdm_0==gwdm:
            kc=kc_0
        else:
            kc=1
        gwdm_0=gwdm
        #start
        for n in range(0, 6):
            kh_3 = '0' + str(n)
            for intkch in range(kc, 250):
                kh_2 = int_str(intkch)###拼接字符串 001
                kh = '2019' + kh_2 + kh_3 + kh_4
                tit = cjcx(kh, xm)
                if tit == '成绩查询':
                    print('查到成绩')
                    kc_0=intkch
                    cj = driver.find_elements_by_xpath("//div[contains(@class,'STYLE88 style9')] ")  # //div[contains(@class,’xxx’)]
                    zcj = cj[3].text
                    driver.back()
                    break
            if tit == '成绩查询':
                xx_list.append(zcj)
                xx_list.append('考号：  ' + str(kh))
                csvFile = open("a1_out.csv", "a",encoding='UTF-8',newline='')
                writer = csv.writer(csvFile)
                writer.writerow(xx_list)
                csvFile.close()
                print(kh,xm)
                break

