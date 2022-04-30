def legendreStart(function, l_range: float, u_range: float, n: int):
    points = [[-(1 / 3) ** .5, ((1 / 3) ** .5)],
              [-(3 / 5) ** .5, 0, ((3 / 5) ** .5)],
              [-((3 / 7 + 2 / 7 * (6 / 5) ** .5) ** .5), -((3 / 7 - 2 / 7 * (6 / 5) ** .5) ** .5),
               (3 / 7 - 2 / 7 * (6 / 5) ** .5) ** .5, (3 / 7 + 2 / 7 * (6 / 5) ** .5) ** .5],
              [-(((5 + 2 * (10 / 7) ** .5) ** .5) / 3), -(((5 - 2 * (10 / 7) ** .5) ** .5) / 3), 0,
               ((5 - 2 * (10 / 7) ** .5) ** .5) / 3, ((5 + 2 * (10 / 7) ** .5) ** .5) / 3]]
    weights = [[1, 1],
               [5 / 9, 8 / 9, 5 / 9],
               [(18 - 30 ** .5) / 36, (18 + 30 ** .5) / 36, (18 + 30 ** .5) / 36, (18 - 30 ** .5) / 36],
               [(322 - 13 * 70 ** .5) / 900, (322 + 13 * 70 ** .5) / 900, 128 / 225,
                (322 + 13 * 70 ** .5) / 900, (322 - 13 * 70 ** .5) / 900]]

    result = 0
    for i in range(n):
        # https://ftims.edu.p.lodz.pl/pluginfile.php/164431/mod_resource/content/2/Fortuna%20Macukow%20Wasowski.pdf
        # str 179
        t = ((l_range + u_range) / 2) + ((u_range - l_range) / 2) * points[n - 2][i]
        result += weights[n - 2][i] * function(t)

    return result * ((u_range - l_range) / 2)
