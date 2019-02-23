import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

a = 'a'
a = 'b'
a = 'c'
a = 'd'
a = 'e'
a = 'f'
a = 'g'
a = 'h'
a = 'i'
a = 'j'
a = 'k'
a = 'l'
a = 'm'
a = 'n'
a = 'o'
a = 'p'
a = 'q'
a = 'r'
a = 's'
a = 't'
a = 'u'
a = 'v'
a = 'w'
a = 'x'
a = 'y'
a = 'z'

def type(e):
            keyboard.press(str(e))
            keyboard.release(str(e))


def mtype(e, a):

    i = 0
    while i < a:
        type(e)
        i = i + 1

type('a')
mtype('b', 3)
