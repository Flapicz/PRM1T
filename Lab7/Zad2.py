
def read_file(plik):
    lista = []
    for line in plik:
        lista.append(line)
    return lista




if __name__ == '__main__':
    iplik0 = input('Podaj nazwe pliku wejsciowego')
    iplik1 = input('Podaj nazwe pliku wyjsciowego')
    sep0 = input("Podaj nazwe seperatora ktory chcesz zastapic")
    sep1 = input("Podaj nazwe nowego seperatora")

    plik0 = open(iplik0, 'r')
    read_file(plik0)

