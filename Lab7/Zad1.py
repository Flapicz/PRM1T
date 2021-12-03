
def rozdziel_zbiory(string):
    string = string.strip(' ')
    zbior1 = string[string.find('{')+1:string.find('}')]
    zbior2 = string[string.rfind('{')+1:string.rfind('}')]
    operator = string[string.find('}')+1:string.rfind('{')]
    zbior11 = []
    zbior22 = []

    for char in zbior1:
        if char == ' ':
            continue
        elif char == ',':
            continue
        else:
            zbior11.append(char)

    for char in zbior2:
        if char == ' ':
            continue
        elif char == ',':
            continue
        else:
            zbior22.append(char)

    #print(zbior11)
    #print(zbior22)
    #print(operator)

    return zbior11, zbior22, operator


def dodaj_zbiory(zbior1, zbior2, operator):
    if operator == '+':
        wynik = zbior1
        for char in zbior2:
            x=0
            for char2 in wynik:
                if char == char2:
                    x=1
                    break
                else:
                    continue
            if x == 0:
                wynik.append(char)

    if operator == '-':
        wynik = zbior1
        for char in zbior2:
            x=0
            for char2 in wynik:
                if char == char2:
                    x=1
                    break
                else:
                    continue
            if x == 1:
                wynik.remove(char)

    if operator == '*':
        wynik = []
        for char in zbior2:
            x=0
            for char2 in zbior1:
                if char == char2:
                    x=1
                    break
                else:
                    continue
            if x == 1:
                wynik.append(char)
    print(wynik)



if __name__ == '__main__':
    string = input("Podaj zbiory")
    baza = rozdziel_zbiory(string)
    dodaj_zbiory(baza[0], baza[1], baza[2])
