lista = ['jeden', 'dwa', 'dwa', 'jeden', 'trzy', 'jeden', 'cztery', 'zero',]

print("Liczba wyrazow w liscie:", len(lista))

liczba_wyrazow = 0
miejsce_wyrazow = []

for i in range(len(lista)):
    if lista.count(lista[i]) > liczba_wyrazow:
        liczba_wyrazow = lista.count(lista[i])
        wyraz = lista[i]

for i in range(len(lista)):
    if wyraz == lista[i]:
        miejsce_wyrazow.append(i)

print('Najczesciej wystepujacy element to "', wyraz, '" (', liczba_wyrazow, 'razy )')
print('Wystepuje na miejscach:', miejsce_wyrazow)

for i in range (liczba_wyrazow):
    lista.remove(wyraz)

print(lista)

lista.insert(0, lista[0])
lista.append(lista[0])

print(lista)

def sprawdz_powtorki():
    for i in range(len(lista)):
        if lista.count(lista[i]) > 1:
            return lista[i]
    return False

lista.sort()
for i in range(len(lista)):
    x = sprawdz_powtorki()
    if x != False:
        lista.remove(x)

print(lista)

lista2 = []
n = 0
if len(lista) % 2 == 0:
    m = len(lista)/2
else:
    m = len(lista)/2 + 1

for i in range(int(m)):
    lista2.append(lista[n])
    n = n + 2

n = 1

for i in range(int(len(lista)/2)):
    lista2.append(lista[n])
    n = n + 2

print(lista2)
