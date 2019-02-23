import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

def typeit():
    sentence = input("Enter what you would like to type: ")
    sentenceArr = list(sentence)
    print("Typing in 5 seconds...")
    sleep(5)
    for i in range(len(sentenceArr)):
        sleep(1/900)
        keyboard.press(sentenceArr[i])
        keyboard.release(sentenceArr[i])
    print("Done!")
    typeit()
typeit()
