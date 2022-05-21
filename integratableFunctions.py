from math import e
from math import sin


def fun_1(x):
    return x ** 2 + 3


def fun_2(x):
    return x ** .5


def fun_3(x):
    return e ** x


def fun_4(x):
    return sin(x)


def fun_5(x):
    if x == 0:
        return 0
    return sin(1/x)
