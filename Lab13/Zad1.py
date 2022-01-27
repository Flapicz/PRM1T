import pandas as pd
import numpy as np


def count_element(column, value):
    return file[file[column] == value].shape[0]


if __name__ == '__main__':
    #zadanie 1
    file = pd.read_csv('chess_games.csv')
    size = file.shape[0]
    print('Liczba rozgrywek:', size)

    #zadanie 2
    print('Wygrana bialych:', round(count_element('winner', 'white') / size * 100, 1), '%')
    print('Wygrana czarnych:', round(count_element('winner', 'black') / size * 100, 1), '%')
    print('Remis:', round(count_element('winner', 'draw') / size * 100, 1), '%')

    #zadanie 4
    zad4 = file[['victory_status', 'white_rating', 'black_rating']]
    zad4 = zad4.groupby(['victory_status']).mean()
    print(zad4)
