# -- coding:utf-8 --
import requests
import pymysql
def insert_mysql(c_xh,c_wzip,c_ip,c_port):
    # 打开数据库连接
    db = pymysql.connect("119.27.184.139", "china", "chinaqin123", "china")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 更新语句
    sql = "INSERT INTO ip_jc (xh,wzip,ip,port) VALUES ('%d','%s','%s','%s')" % (c_xh,c_wzip,c_ip,c_port)
    cursor.execute(sql)
    db.commit()
    db.close()
from urllib import request
res = request.urlopen(
        'http://dev.kdlapi.com/api/getproxy/?orderid=916101486940366&num=300&protocol=1&method=2&an_an=1&an_ha=1&sep=3')
result = res.read()
result = str(result, encoding="utf-8")
li = result.split(" ")
#IPAgents = ["163.204.241.242:9999"]
proxies_list=li
ip_list=[]
url = 'http://icanhazip.com'
nm=23
for proxy_ip in proxies_list:
    print(proxy_ip)
    # print(proxies_list)
    proxies = {'http': proxy_ip}
    try:
        wb_data = requests.get(url=url, proxies=proxies)
        flag = True
    except:
        proxies_list.remove(proxies['http'])
        flag = False

    if flag:
        ip_list.append(proxies['http'])
        print(proxies,'有效')
        c_xh=nm
        c_wzip=proxy_ip
        cc=proxy_ip.split(":")
        c_ip=cc[0]
        c_port=cc[1]
        #print(c_xh, c_wzip, c_ip, c_port)
        insert_mysql(c_xh, c_wzip, c_ip, c_port)
        print('插入数据库成功！ 共检测到: '+str(c_xh))
        nm+=1
#print(ip_list)
