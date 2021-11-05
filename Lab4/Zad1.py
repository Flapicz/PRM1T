import math

y = 2


def maclaurin(x, N):
    wynik = 0
    for i in range(N):
        wynik = wynik + ((-1) ** i / math.factorial(2 * i) * x ** (2 * i))
    return wynik


print(maclaurin(float(input("Podaj x")), int(input("Podaj N"))))

for i in range(5):
    print("N =", y, " x =", maclaurin(math.pi / 4, y))
    y = y + 2
