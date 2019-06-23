import pytesseract
from PIL import Image
tessdata_dir_config = '--tessdata-dir "F://tool//Tesseract-OCR//tessdata"'
def to_ocr(image_path):
    image = Image.open(image_path)
    code = pytesseract.image_to_string(image,lang = 'eng', config=tessdata_dir_config)
    return (code)