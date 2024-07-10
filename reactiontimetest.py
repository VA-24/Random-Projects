import cv2
import numpy as np
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

x = 100
y = 270
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://humanbenchmark.com/tests/reactiontime')
pyautogui.moveTo(x, y)


#time delay to switch difficulty to hard mode
time.sleep(2)
box_coordinates = (100, 270, 100, 100)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
lower_green = np.array([36, 25, 25])
upper_green = np.array([86, 255, 255])
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

def is_color_in_range(image, lower_bound, upper_bound):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    return cv2.countNonZero(mask) > 0

while True:
    screenshot = pyautogui.screenshot(region=box_coordinates)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    if is_color_in_range(frame, lower_green, upper_green):
        print('green')
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()


