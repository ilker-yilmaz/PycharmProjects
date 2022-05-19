from lib2to3.pgen2 import driver

from pkg_resources import require

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

driver.get("http://localhost:3000/")

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('2uU3zk.png')))
