from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
import re
import pyautogui

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome()

keyboard = Controller()
driver.get('https://arithmetic.zetamac.com/')

#time delay to switch difficulty to hard mode


def solve():
    problem = driver.find_element(By.CLASS_NAME, 'problem')
    problem = problem.text
    print(problem)

    operators = ['–', '+', '÷', '×']
    numbers = [int(num) for num in re.findall(r'\b\d+\b', problem)]

    for operator in operators:
        if operator in problem:
            if operator == '–':
                answer = numbers[0] - numbers[1]
                text_answer = str(answer)
                keyboard.type(text_answer)
                print(text_answer)
            elif operator == '+':
                answer = numbers[0] + numbers[1]
                text_answer = str(answer)
                keyboard.type(text_answer)
                print(text_answer)
            elif operator == '÷':
                answer = numbers[0] // numbers[1]
                text_answer = str(answer)
                keyboard.type(text_answer)
                print(text_answer)
            elif operator == '×':
                answer = numbers[0] * numbers[1]
                text_answer = str(answer)
                keyboard.type(text_answer)
                print(text_answer)



itr = 0
while True:
    if(itr == 0):
        time.sleep(2)
    solve()
    itr = itr + 1


