

def read_file(file):
    lista = []
    for line in file:
        lista.append(line.split())
    return lista

def decipher(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(chr(int(lista[i][0])))
    return lista2

def save_to_file(lista2):
    new_file = open("result.txt", "w")
    x = 0
    for i in range(len(lista2)):
        new_file.write(lista2[i])
        x += 1
        if x == 120:
            new_file.write("\n")
            x = 0



file = open("code.txt", "r")
if __name__ == "__main__":
    lista = read_file(file)
    print(lista)
    file.close()
    lista2 = decipher(lista)
    print(lista2)
    save_to_file(lista2)

