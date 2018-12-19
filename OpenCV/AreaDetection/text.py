import cv2
from PIL import Image
import pytesseract

im=Image.open("sample14.png")
text=pytesseract.image_to_string(im)

print(text)