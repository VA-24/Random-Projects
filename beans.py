from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
import pyautogui
import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome()

keyboard = Controller()
driver.get('https://beanbeanbean.com/html/category/math/addition.html')

#time delay to switch difficulty to hard mode
time.sleep(2)


def play():
    try:
        first_number = driver.find_element(By.XPATH, '//p[@id = \'pFirstNumber\']')
        first_number = int(first_number.text)
        second_number = driver.find_element(By.XPATH, '//p[@id = \'pSecondNumber\']')
        second_number = int(second_number.text)
        ans = first_number + second_number
        text_ans = str(ans)

        keyboard.type(text_ans)
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    except:
        button = driver.find_element(By.CSS_SELECTOR, 'button[id=\'buttonDonate\'][style=\'display: block;\']')
        button.click()
        time.sleep(4)
        button = driver.find_element(By.CSS_SELECTOR, 'button[id=\'buttonRestart\'][style=\'display: block;\']')
        button.click()
        time.sleep(2)
        pyautogui.click(365, 589)
        pyautogui.click(365, 589)

while True:
    itr = 0
    if(itr == 0):
        time.sleep(1)
    play()
    itr = itr + 1
