import pytesseract
from PIL import Image
if __name__ == '__main__':
    aa = pytesseract.image_to_string('789.png',lang='eng')
    print(aa)