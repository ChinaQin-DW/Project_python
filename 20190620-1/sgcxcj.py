# -- coding:utf-8 --
from selenium import webdriver
import time
import pytesseract
from PIL import Image
import pymysql
def select_mysql():
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT ip,port FROM ip_jc ;"
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results
def cxcj(driver,c_kh):
    for mm in range(1,10):
        driver.find_element_by_id("number").clear()
        driver.find_element_by_id("number").send_keys(c_kh)  # 考号
        driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
        tit = (driver.title)
        zfc = driver.find_element_by_xpath(
            "//span[contains(@style, 'font-size:16px; font-weight:bold; color:#FF0000')]")  # 获取是否警告ip
        if tit == '成绩查询':
            driver.close()
            kzhs='0'
            break
        elif zfc.text == '您访问系统过于频繁，请30分钟后登录系统进行查询！':
            kzhs = '1'
            break
        else:
            driver.find_element_by_id("button").click()  # 上一步
    driver.close()
    return kzhs

##字符串转换函数
def int_str(intkch):
    if intkch < 10:
        kh_2 = '00' + str(intkch)
    elif intkch < 100:
        kh_2 = '0' + str(intkch)
    elif intkch < 1000:
        kh_2 = str(intkch)
    return kh_2
###
xm='冉孟夏'
kh_4='559'
ip_list=select_mysql()
lx1=0
kc1=0
for n in ip_list:
    c_ip=n[0]
    c_port=n[1]
    profile = webdriver.FirefoxOptions()
    profile.add_argument('-headless')  # 设置无头模式
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.http', c_ip)  # IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型
    profile.set_preference('network.proxy.http_port', c_port)  # PORT为代理服务器端口号:如，9999，整数类型
    driver = webdriver.Firefox(options=profile)
    driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
    time.sleep(5)
    element = driver.find_element_by_xpath("//img[contains(@src, '/2019cjfb/register/image.jsp')]")
    element.screenshot('yzm_1.png')
    img = Image.open('yzm_1.png')  # 根据地址，读取图片
    yzm = pytesseract.image_to_string(img)  # 读取里面的内容
    driver.find_element_by_id("yznumber").send_keys(yzm)  # 验证码
    driver.find_element_by_id("name").send_keys(xm)  # 名字
    for n in range(lx1,5):
        kh_3 = '0' + str(n)  # 编号  00 01 02
        for intkch in range(kc1,300):
            kh_2 = int_str(intkch)  ###拼接字符串 001
            kh = '2019' + kh_2 + kh_3 + kh_4
            print('start: ', kh, xm)
        resu = cxcj(driver,kh)#
        break
    if resu=='0':
        print('查到成绩，信息为：',kh,xm)
        break
