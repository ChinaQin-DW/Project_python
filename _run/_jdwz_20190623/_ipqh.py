# -- coding:utf-8 --
from selenium import webdriver
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