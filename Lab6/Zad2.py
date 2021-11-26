def find_letters(wyraz):
    min = len(wyraz)
    max = 0
    for i in range(len(wyraz)):
        if wyraz[i].isalpha():
            if i > max:
                max = i
            if i < min:
                min = i
    lista = [min, max]
    #print(lista)
    return lista


def funkcja(wyraz, minmax):
    i = 0
    for chr in wyraz:
        if chr.isalpha():
            i += 1
            continue
        elif i < minmax[0]:
            #print('usun', chr)
            wyraz = wyraz[:i] + wyraz[(i + 1):]
            i -= 1
            minmax[1] -= 1
        elif i > minmax[1]:
            #print('usun', chr)
            wyraz = wyraz[:i] + wyraz[(i + 1):]
            i -= 1
        i += 1
    #print(wyraz)


if __name__ == "__main__":
    with open('fabryka.txt', 'r') as file:
        wyraz = str(input("Podaj wyraz"))
        for line in file:
            temp = line.split()
            #print(temp)
            for wyraz in temp:
                #print(wyraz)
                minmax = find_letters(wyraz)
                funkcja(wyraz, minmax)

