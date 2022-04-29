import Simpson as sim
import integratableFunctions as inF


def main():
    print(sim.simpsonStart(inF.fun_1, 0, 4, 0.0001))
    return


if __name__ == '__main__':
    main()