from operator import le


def f(x):
    liczba = 0
    liczba = int(x[0]) + int(x[1]) + int(x[2])
    reszta = liczba % 7
    if reszta == int(x[3]):
        return True
    else:
        return False

