from selenium import webdriver
import pyautogui
import time
import math


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome()

driver.get('https://neal.fun/perfect-circle/')
time.sleep(3)

time.sleep(2)
radius = 300
num_points = 40

dot_x, dot_y = 668, 622
points = []
for i in range(num_points):
    angle = 2 * math.pi * i / num_points
    x = dot_x + radius * math.cos(angle)
    y = dot_y + radius * math.sin(angle)
    points.append((x, y))

pyautogui.moveTo(points[0])
pyautogui.mouseDown(button='left')

for point in points:
    pyautogui.moveTo(point)
    time.sleep(0.001)

pyautogui.moveTo(points[0])
pyautogui.mouseUp(button='left')

time.sleep(1)
