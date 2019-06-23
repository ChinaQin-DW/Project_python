# -- coding:utf-8 --
from selenium import webdriver
import time
profile = webdriver.FirefoxOptions()
profile.add_argument('-headless') #设置无头模式
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '103.239.145.109')  # IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型
profile.set_preference('network.proxy.http_port', 54034)  # PORT为代理服务器端口号:如，9999，整数类型
browser = webdriver.Firefox(options=profile)
browser.get('http://icanhazip.com')
dd=browser.find_element_by_xpath("//html") #/html/body/pre
print('11',dd.text)
browser.close()
time.sleep(5)
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', '191.102.83.149')  # IP为你的代理服务器地址:如‘127.0.0.0’，字符串类型
profile.set_preference('network.proxy.http_port', 80)  # PORT为代理服务器端口号:如，9999，整数类型
browser = webdriver.Firefox(options=profile)
browser.get('http://icanhazip.com')
dd=browser.find_element_by_xpath("//html") #/html/body/pre
print('22',dd.text)
browser.close()