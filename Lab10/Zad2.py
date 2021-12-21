import numpy as np


def licz():
    x = np.linspace(z[0], z[1], num=N)
    g2 = np.polyval(g, x)
    h2 = np.polyval(h,x)
    w = np.array([x, g2/h2])
    print(w)

def wyjatki():
    assert len(g.shape) == 1 and len(h.shape) == 1, "Tablice wspolczynnikow wielomianow musza byc jednowymiarowe"
    assert z.shape == (2,) and z[0] != z[1], "Krance przadzialu musza byc rozne"
    assert N > 1 and type(N) == int, "N musi byc liczba calkowita wieksza od 1"


if __name__ == '__main__':
    g = np.array([4, -3, 2, 1])
    h = np.array([2, 0, 1])
    z = np.array([2, 3])
    N = 11
    wyjatki()
    licz()
