from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys, string, re

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


keyboard = Controller()
driver.get('https://wordle.jonyork.net/game/tvbis')

#time delay to switch difficulty to hard mode
time.sleep(2)

keyboard.type('glent')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.1)
keyboard.type('brick')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.1)
keyboard.type('jumpy')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.1)
keyboard.type('vozhd')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.1)
keyboard.type('waqfs')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.1)

in_word = ''
not_in_word = ''
yellow_letters = []
placement = ['_', '_', '_', '_', '_']
placement_str = ''

letters = driver.find_elements(By.CLASS_NAME, 'letter')
letters = letters[0:29]

for letter in letters:
    rgb = letter.get_attribute('style')[48: -1]
    if rgb == '(83, 141, 78)':
        in_word += letter.text.lower()
        index = letters.index(letter)
        if index in range(0, 5):
            placement[index] = letter.text.lower()
        elif index in range(5, 10):
            placement[index - 5] = letter.text.lower()
        elif index in range(10, 15):
            placement[index - 10] = letter.text.lower()
        elif index in range(15, 20):
            placement[index - 15] = letter.text.lower()
        elif index in range(20, 25):
            placement[index - 20] = letter.text.lower()

    elif rgb == '(181, 159, 59)':
        in_word += letter.text.lower()
        location = ''
        location += letter.text.lower()
        index = letters.index(letter)
        if index in range(0, 5):
            location += str(index)
        elif index in range(5, 10):
            location += str(index - 5)
        elif index in range(10, 15):
            location += str(index - 10)
        elif index in range(15, 20):
            location += str(index - 15)
        elif index in range(20, 25):
            location += str(index - 20)

        yellow_letters.append(location)
    elif rgb == '(58, 58, 60)':
        not_in_word += letter.text.lower()

for element in placement:
    placement_str += element

print(in_word, not_in_word, placement_str, yellow_letters)

def split(word):
    return [char for char in word]

dictionary = open("words.txt", "r")
words = dictionary.readlines()
dictionary.close()

solutions = []

for word in words:
   solutions.append(word.strip())

if in_word != '?':
    solutions = [x for x in solutions if all(y in x for y in in_word)]

print(solutions)

if not_in_word != '?':
    solutions = [x for x in solutions if all(y not in x for y in not_in_word)]

placement_str = placement_str.replace("_", ".")

placement_pattern = "^" + placement_str + "$"
pattern = re.compile(placement_pattern)


for i in range(len(solutions) - 1, -1, -1):
    word = solutions[i]
    if pattern.match(word):
        for letter in yellow_letters:
            if word[int(letter[1])] == letter[0]:
                solutions.pop(i)
                break

time.sleep(0.2)
keyboard.type(solutions[0])
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(0.2)
