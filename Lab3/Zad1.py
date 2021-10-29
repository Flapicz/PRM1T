N = int(input("Podaj N"))
lista = []

for i in range(N):
    lista.append(int((i + 1) * '1'))

print(lista)
print(type(lista[0]))
