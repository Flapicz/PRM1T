def load_file(file):
    dict = {}
    for line in file:
        tempList = line.split()
        dict[tempList[0]] = tempList[1]
    print(dict)
    return dict


def check(dict):
    x = input("Podaj liczbe")
    print(x in dict)
    y = x in dict
    if y is True:
        print(dict[x])
    else:
        print("Nieprawidłowa liczba")


if __name__ == "__main__":
    file = open("midi_instruments.txt", "r")
    dict = load_file(file)
    file.close()
    check(dict)
