# -- coding:utf-8 --
from selenium import webdriver
import time
###options.add_argument('-headless')
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '85.232.248.9')
profile.set_preference('network.proxy.http_port', 8080)  # int
profile.set_preference("network.proxy.share_proxy_settings", True)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://httpbin.org/ip')
time.sleep(10)
c_ip = '89.43.6.114:8080'  # ip格式"127.0.0.1:80"
def change_ip(driver,c_ip):
    ip=c_ip
    driver.get("about:config");
    # js代码
    setupScript = '''var prefs = Components.classes["@mozilla.org/preferences-service;1"].getService(Components.interfaces.nsIPrefBranch);
    prefs.setIntPref("network.proxy.type", 1);
    prefs.setCharPref("network.proxy.http", "%s");
    prefs.setIntPref("network.proxy.http_port", "%s");
    prefs.setCharPref("network.proxy.ssl", "%s");
    prefs.setIntPref("network.proxy.ssl_port", "%s");
    prefs.setCharPref("network.proxy.ftp", "$%s");
    prefs.setIntPref("network.proxy.ftp_port", "%s");
    ''' % (ip.split(':')[0], ip.split(':')[1], ip.split(':')[0], ip.split(':')[1], ip.split(':')[0], ip.split(':')[1])
    # 执行js
    driver.execute_script(setupScript);
time.sleep(3)
change_ip(driver,c_ip)
time.sleep(3)
driver.get('http://httpbin.org/ip')
c_ip2 = '183.128.149.31:8118'  # ip格式"127.0.0.1:80"
time.sleep(10)
change_ip(driver,c_ip2)
driver.get('http://httpbin.org/ip')

###   85.232.248.9"
##"89.43.6.114, 89.43.6.114"
###183.128.149.31

