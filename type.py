from selenium import webdriver
from pynput.keyboard import Key, Controller
import time
import random



PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

keyboard = Controller()
driver.get('https://monkeytype.com')

time.sleep(5)

words = driver.find_elements_by_class_name("word")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for element in words:
    word = element.text
    lenWord = len(word)
    randIndex = random.randint(0, 200)

    #optimal 48
    if (randIndex > 20):
        for i in range(lenWord):
            keyboard.press(word[i])
            time.sleep(random.uniform(0.0035, 0.05))
            keyboard.release(word[i])
    else:
        wordIndex = random.randint(0, lenWord)
        for i in range(lenWord):
            if (i == wordIndex):
                keyboard.press(random.choice(alphabet))
                time.sleep(random.uniform(0.0035,0.05))
                keyboard.release(random.choice(alphabet))
            else:
                keyboard.press(word[i])
                time.sleep(random.uniform(0.0035, 0.05))
                keyboard.release(word[i])
    time.sleep(random.uniform(0.05, 0.1))
    keyboard.press(Key.space)
    keyboard.release(Key.space)
