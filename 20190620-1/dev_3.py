# -- coding:utf-8 --
import csv
from selenium import webdriver
import time
import pymysql
import sys
c_gwdm=sys.argv[1]  #获取要查询的岗位
print('本次要查询的岗位是：',c_gwdm)
# s数据库查询函数
def select_mysql(s_gwdm):
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT xh,xm,gwdm,kh FROM jdwz_2   WHERE gwdm =%s" % (s_gwdm)
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
    sql = "UPDATE jdwz_2 SET fx = '%s',wzkh='%s' WHERE xh = '%d';" % (c_xh, c_kh, c_cj)
    cursor.execute(sql)
    db.commit()
    db.close()

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
#链接数据库获取要查询的人员信息
cx_tup=select_mysql(c_gwdm) #链接数据库获取要查询的岗位信息
#开始查询
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
    for n in range(0, 5):
        kh_3 = '0' + str(n) #编号  00 01 02
        for intkch in range(kc, 250):
            kh_2 = int_str(intkch)  ###拼接字符串 001
            kh = '2019' + kh_2 + kh_3 + kh_4
            tit = cjcx(kh, xm) #执行模拟操作函数
            if tit == '成绩查询':
                print('查到成绩')
                kc_0 = intkch
                cj = driver.find_elements_by_xpath(
                    "//div[contains(@class,'STYLE88 style9')] ")  # //div[contains(@class,’xxx’)]
                zcj = cj[3].text
                driver.back()
                break
        if tit == '成绩查询':
            update_mysql(xh,kh,zcj)  ##c_xh,c_kh,c_cj
            # xx_list.append(zcj)
            # xx_list.append('考号：  ' + str(kh))
            # csvFile = open("a1_out.csv", "a", encoding='UTF-8', newline='')
            # writer = csv.writer(csvFile)
            # writer.writerow(xx_list)
            # csvFile.close()
            # print(kh, xm)
            break
print(c_gwdm,'   查询完成')

