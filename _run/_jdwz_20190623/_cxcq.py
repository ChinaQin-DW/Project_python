# -- coding:utf-8 --
from selenium import webdriver
import pytesseract
import time
from PIL import Image
tessdata_dir_config = '--tessdata-dir "F://tool//Tesseract-OCR//tessdata"'
def _cxcj(driver,c_kh,c_name):
    yzm_status = driver.find_element_by_id("yznumber").text  ##查看认证码是否为空
    if yzm_status=='':
         element = driver.find_element_by_xpath("//img[contains(@src, '/2019cjfb/register/image.jsp')]")
         element.screenshot('yzm.png')
         image = Image.open('yzm.png')
         yzm_num = pytesseract.image_to_string(image, lang='eng', config=tessdata_dir_config)
         driver.find_element_by_id("yznumber").send_keys(yzm_num)  # 验证码
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("number").clear()
    driver.find_element_by_id("number").send_keys(c_kh)  # 考号
    driver.find_element_by_id("name").send_keys(c_name)  # 名字
    driver.find_element_by_xpath("//img[contains(@onclick, 'return sub();')]").click()  # 登录
    time.sleep(3)
    tit = (driver.title)
    zfc = driver.find_element_by_xpath(
            "//span[contains(@style, 'font-size:16px; font-weight:bold; color:#FF0000')]")  # 获取是否警告ip
    if tit == '成绩查询':
        driver.close()
        kzhs='0'
    elif zfc.text == '您访问系统过于频繁，请30分钟后登录系统进行查询！':
        kzhs = '1'

    else:
        driver.find_element_by_id("button").click()  # 上一步
        kzhs = '2'
    return kzhs