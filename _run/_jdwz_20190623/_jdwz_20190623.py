# -- coding:utf-8 --
from _conn_mysql import select_mysql
from _ocr import to_ocr
from selenium import webdriver
import time
from _ipqh import change_ip
from _cxcq import _cxcj
##字符串转换函数
def int_str(intkch):
    if intkch < 10:
        intkch = '00' + str(intkch)
    elif intkch < 100:
        intkch = '0' + str(intkch)
    elif intkch < 1000:
        intkch = str(intkch)
    return intkch

### start
s_xm='冉孟夏'
s_kh='559'
ip_list=select_mysql()
ip_max=len(ip_list) ## ip个数
ip_n=0
##设置浏览器信息
#profile.add_argument('-headless')  # 设置无头模式
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '192.189.28.9')
profile.set_preference('network.proxy.http_port', 8080)  # int
profile.set_preference("network.proxy.share_proxy_settings", True)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
url_status=0
for n in range(0,5):
    kh_3 = '0' + str(n)  # 编号  00 01 02
    for intkch in range(0, 300):
        kh_2 = int_str(intkch)  ###拼接字符串 001
        kh = '2019' + kh_2 + kh_3 + s_kh
        print('start: ', kh, s_xm)
        #打开浏览器
        while url_status==0:
            try :
                driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
                url_status=1
            except Exception:
                change_ip(driver, ip_list[n][0])
                n+=1
        time.sleep(2)
        ##执行查询操作
        kzhs = _cxcj(driver, kh, s_xm)  # 查询成绩
        while kzhs=='1':
            change_ip(driver, ip_list[n][0])
            n += 1
            try :
                driver.get('http://211.166.76.62/2019cjfb/register/cjcx.jsp')
                kzhs = _cxcj(driver, kh, s_xm)  # 查询成绩
            except Exception:
                print(ip_list[n][0],'不可用')

        if kzhs == '0':
            print('查到了成绩：',kh, s_xm)
            break

    if kzhs == '0':
        break



