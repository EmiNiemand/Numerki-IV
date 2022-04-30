import Simpson as sim
import Legendre as leg
import integratableFunctions as inF


def main():
    fun = None
    while fun is None:
        fun = int(input("Podaj numer funkcji [1-5]: "))
        match fun:
            case 1: fun = inF.fun_1
            case 2: fun = inF.fun_2
            case 3: fun = inF.fun_3
            case 4: fun = inF.fun_4
            case 5: fun = inF.fun_5
            case _: fun = None

    l_range = float(input("Podaj dolny zakres: "))
    u_range = float(input("Podaj górny zakres: "))
    if l_range > u_range:
        pom = l_range
        l_range = u_range
        u_range = pom

    accuracy = float(input("Podaj wartość dokładności: "))

    node = 0
    while node not in list(range(2, 6)):
        node = int(input("Podaj liczbę węzłów [2-5]: "))

    print("Wynik Simpsonem =", sim.simpsonStart(fun, l_range, u_range, accuracy))
    print("Wynik Legendrem =", leg.legendreStart(fun, l_range, u_range, node))
    return


def main2():
    print("Wynik Simpsonem =", sim.simpsonStart(inF.fun_5, 0, 4, 0.000000001))
    print("Wynik Legendrem =", leg.legendreStart(inF.fun_5, 0, 4, 5))


if __name__ == '__main__':
    main()
    # main2()
