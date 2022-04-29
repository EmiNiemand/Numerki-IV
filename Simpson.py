import math


def simpsonStart(function, l_range: float, u_range: float, accuracy: float):
    n = 2
    last_result = -1
    while True:
        h = calculateH(l_range, u_range, n)
        fx0 = function(l_range)
        fxn = function(u_range)

        evenX = 0
        oddX = 0
        for i in range(2, n + 1, 2):
            evenX += function(calculateH(u_range, l_range, n, i))
            oddX += function(calculateH(u_range, l_range, n, i - 1))

        result = calculateSimpson(h, fx0, fxn, evenX, oddX)
        if math.fabs(result - last_result) < accuracy:
            return result

        last_result = result
        n *= 2


def calculateH(l_range: float, u_range: float, n: float, i: float = 1):
    return (u_range - l_range) * i / n


def calculateSimpson(h: float, fx0: float, fxn: float, evenX: float, oddX: float):
    return (h / 3) * (fx0 + fxn + 4 * evenX + 2 * oddX)

