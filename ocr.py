import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def convert(img):
    img = Image.open(img)
    text = pytesseract.image_to_string(img)
    return text

