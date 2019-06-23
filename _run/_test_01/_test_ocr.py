# -- coding:utf-8 --
import pytesseract
from PIL import Image
from PIL import ImageEnhance
img = Image.open('jt001\ima_1112jpeg')  # 根据地址，读取图片
code = pytesseract.image_to_string(img)  # 读取里面的内容
print(code)