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
t = 't'
u = 'u'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'
SPACE = ' '

def type(key):
            keyboard.press(str(key))
            keyboard.release(str(key))


def mtype(key, time):

    amount = 0
    while amount < time:
        type(key)
        amount = amount + 1

type(a)
mtype(b, 3)
