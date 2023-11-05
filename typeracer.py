import os
import time
from PIL import Image
import pytesseract
from pynput.keyboard import Key, Controller

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/va648/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
keyboard = Controller()
base_dir = 'C:/Users/va648/OneDrive/Pictures/Screenshots'

pics = os.listdir(base_dir)
time.sleep(5)
pics_new = os.listdir(base_dir)

extra_element = list(set(pics_new) - set(pics))
print(extra_element[0])

ss_load = Image.open(base_dir + '/' + extra_element[0])
text = pytesseract.image_to_string(ss_load)

if text[0] == '[':
    text = text[1: -1]
print(text)
lines = text.splitlines()
new_text = ''
for line in lines:
    new_text = new_text + line + ' '

time.sleep(1)
for i in range(len(new_text)):
    keyboard.type(new_text[i])
    time.sleep(0.003)