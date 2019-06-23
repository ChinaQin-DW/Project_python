import pytesseract
from PIL import Image
tessdata_dir_config = '--tessdata-dir "F://tool//Tesseract-OCR//tessdata"'
image = Image.open(r'image\a.png')
code = pytesseract.image_to_string(image,lang = 'eng', config=tessdata_dir_config)
print(code)