import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

wpm = 100

def typeit():
        sentence = input("Enter what you would like to type: ")
        sentenceArr = list(sentence)
        print("Typing in 5 seconds...")
        sleep(5)
        for i in range(len(sentenceArr)):
            sleep((len(sentenceArr)/5/wpm*60)/len(sentenceArr))
            keyboard.press(sentenceArr[i])
            keyboard.release(sentenceArr[i])
        print("Done!")
        Main()

def typelevel():
        level = input("Enter the level #: ")
        file = open('levels/'+str(level)+'.txt', 'r')
        totype = file.read()
        sentenceArr = list(totype)
        print("Typing in 5 seconds...")
        sleep(5)
        for i in range(len(sentenceArr)):
            sleep((len(sentenceArr)/5/wpm*60)/len(sentenceArr))
            keyboard.press(sentenceArr[i])
            keyboard.release(sentenceArr[i])
        print("Done!")
        Main()

def Main():
    levelornot = input("Would you like to type a custom thing or a level? (C or L) ").lower()

    if(levelornot == 'l'):
        typelevel()
    else:
        typeit()

Main()



