import warnings

import pandas as pd
import numpy as np
import warnings as wrn
import os


def zad1(filename, winner):
    if os.path.isfile(filename) == False:
        raise AssertionError('Brak pliku')
    global file
    file = pd.read_csv(filename)
    size = file.shape[0]
    if size > 20000:
        warnings.warn('Plik jest bardzo duzy', UserWarning)
    print('Liczba rozgrywek:', size)
    winrate = count_element('winner', winner) / size * 100
    print('Wygrany:', winner, round(winrate, 2), '%')
    return size, winrate


def count_element(column, value):
    return file[file[column] == value].shape[0]


if __name__ == '__main__':
    # filename = input("Podaj nazwe pliku")
    # winner = input('Podaj wygranego')
    filename = 'chess_games.csv'
    winner = 'white'
    zad1(filename, winner)
