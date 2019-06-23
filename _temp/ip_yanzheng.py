import requests
import threading
from lxml import etree
def thread_write_proxy(proxy):
    with open("./ip_proxy.txt", 'a+') as f:
        print("正在写入：", proxy)
        f.write(proxy + '\n')
        print("录入完成！！！")

#添加线程模式
def thread_test_proxy(proxy):
    url = "http://www.baidu.com/"
    header = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    try:
        response = requests.get(
            url, headers=header, proxies={"http": proxy}, timeout=1)
        if response.status_code == 200:
            print("该代理IP可用：", proxy)
            #normal_proxies.append(proxy)
            thread_write_proxy(proxy)
        else:
            print("该代理IP不可用：", proxy)
    except Exception:
        print("该代理IP无效：", proxy)
        pass