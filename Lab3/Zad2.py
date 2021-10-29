
lista = ['kajak', 'dom', 'palindrom', 'ada', '123321', 'kajak', 'KAJAK', 'AdA', 'bOb']
palind = []


def sprawdz_powtorki():
    for k in range (len(palind)):
        if palind[k] == wyraz:
            return False
    return True


for i in range (len(lista)):
    wyraz = str.lower(lista[i])
    x = -1
    for j in range (len(wyraz)):
        if j == len(wyraz) - 1:
            if sprawdz_powtorki() == True:
                palind.append(wyraz)
                break
        if wyraz[j] == wyraz[x]:
            x -= 1
            continue
        else:
            print(lista[i], "nie jest palindromem")
            break
print (sorted(palind))