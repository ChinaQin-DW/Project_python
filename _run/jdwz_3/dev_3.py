# -- coding:utf-8 --
import csv
from selenium import webdriver
import time
import pymysql
import sys
import pytesseract
from PIL import Image
c_gwdm=sys.argv[1]  #获取要查询的岗位
print('本次要查询的岗位是：',c_gwdm)
# s数据库查询函数
def select_mysql(s_gwdm):
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT xh,xm,gwdm,kh FROM jdwz_2   WHERE gwdm =%s and fx is null ;" % (s_gwdm)
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
#数据库更新操作
def update_mysql(c_xh,c_kh,c_cj):
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = "UPDATE jdwz_2 SET fx = '%s',wzkh='%s' WHERE xh = '%d';" % (c_cj,c_kh,c_xh)
    cursor.execute(sql)
    db.commit()
    db.close()

#打开浏览器
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
#browser = webdriver.Firefox(options=options)
driver=webdriver.Firefox(options=options)

driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
# 等待首次输入验证码
time.sleep(1)
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
##字符串转换函数
def int_str(intkch):
    if intkch < 10:
        kh_2 = '00' + str(intkch)
    elif intkch < 100:
        kh_2 = '0' + str(intkch)
    elif intkch < 1000:
        kh_2 = str(intkch)
    return kh_2

def open_fire(s_kh,s_xm,c_driver,cz_num):
    if cz_num>9 :
        driver=c_driver
        cz_num=0
    else:
        c_driver.close()
        time.sleep(1)
        print('重新打开浏览器')
        driver = webdriver.Firefox(options=options)
        driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
    cz_num += 1
    element = driver.find_element_by_xpath("//img[contains(@src, '/2019cjfb/register/image.jsp')]")
    element.screenshot('yzm_1.png')
    img = Image.open('yzm_1.png')  # 根据地址，读取图片
    yzm = pytesseract.image_to_string(img)  # 读取里面的内容
    driver.find_element_by_id("number").clear()
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("number").send_keys(s_kh)  # 考号
    driver.find_element_by_id("name").send_keys(s_xm)  # 名字
    driver.find_element_by_id("yznumber").send_keys(yzm)  #验证码
    driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
    tit = (driver.title)
    if tit=='成绩查询':
        cj = driver.find_elements_by_xpath(
            "//div[contains(@class,'STYLE88 style9')] ")  # //div[contains(@class,’xxx’)]
        zcj = cj[3].text
        return '0',zcj,cz_num
    else:
        zfc = driver.find_element_by_xpath(
            "//span[contains(@style, 'font-size:16px; font-weight:bold; color:#FF0000')]")  # 获取是否警告ip
        if zfc.text=='您访问系统过于频繁，请30分钟后登录系统进行查询！':
            return '1',zfc.text,cz_num
        if zfc.text=='登录信息错误或未缴费，请检查！':
            return '2',zfc.text,cz_num



gwdm_0=''
kc_0=1
#链接数据库获取要查询的人员信息
cx_tup=select_mysql(c_gwdm) #链接数据库获取要查询的岗位信息
#开始查询
cz_num=1
for renyuan in cx_tup:
    xx_list = renyuan
    print(renyuan)
    xh=renyuan[0]  #序号 数据库唯一
    xm=renyuan[1]#姓名
    gwdm = renyuan[2]#岗位代码
    kh_4=renyuan[3]#人员序号
    if gwdm_0 == gwdm: #当前和上一个是否是同一个岗位 相同就从上一个考场号开始
        kc = kc_0
    else:
        kc=1  ###开始的序号
    gwdm_0 = gwdm #标记当前的岗位代码
    # start 开始查询
    for n in range(0, 6):
        kh_3 = '0' + str(n) #编号  00 01 02
        for intkch in range(kc, 250):
            kh_2 = int_str(intkch)  ###拼接字符串 001
            kh = '2019' + kh_2 + kh_3 + kh_4
            #tit = cjcx(kh, xm) #执行模拟操作函数
            print('start: ', kh, xm)
            resu=open_fire(kh,xm,driver,cz_num)
            cz_num=int(resu[2])
            print(resu[0],resu[1])
            if resu[0]=='0':
                zcj = resu[1]
                print('查到成绩:',zcj) #查询到成绩
                driver.back()
                break
            # elif resu[0]=='1': #访问受限
            #     driver.quit()
            #     time.sleep(1)
            #     print('重新打开浏览器')
            #     driver = webdriver.Firefox(options=options)
            #     driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
            else:
                driver.find_element_by_id("button").click()  # 上一步

        if resu[0]=='0':
            update_mysql(xh,kh,zcj)  ##c_xh,c_kh,c_cj
            print('更新成功')
            break

print(c_gwdm,'   查询完成')

