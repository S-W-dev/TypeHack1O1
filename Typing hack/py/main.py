import pynput
from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'
h = 'h'
i = 'i'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
o = 'o'
p = 'p'
q = 'q'
r = 'r'
s = 's'
a = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'

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
