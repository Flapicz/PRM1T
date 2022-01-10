import numpy as np
import matplotlib.pylab as plt
import json


def plot(lata,miejsce,kolor,opis):
    plt.plot(data['year'][lata[0]:lata[1]+1],data['life_expectancy'][miejsce][lata[0]:lata[1]+1], kolor, label=opis)

if __name__ == '__main__':
    file = open('expectancy.json')
    data = json.load(file)
    lata1 = [data['year'].index(1955),data['year'].index(2020)]
    lata2 = [data['year'].index(2020),data['year'].index(2060)]
    plot(lata1,'world','-r','Swiat')
    plot(lata1, 'europe', '-g','Europa')
    plot(lata1, 'poland', '-b','Polska')
    plot(lata2, 'world', '--r','')
    plot(lata2, 'europe', '--g','')
    plot(lata2, 'poland', '--b','')
    plt.title('Srednia dlugosc zycia')
    plt.xlabel('Rok')
    plt.legend()
    plt.grid()
    plt.show()

