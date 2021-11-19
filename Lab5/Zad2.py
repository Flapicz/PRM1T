

def load_file(file):
    dict = {}
    for line in file:



if __name__ == "__main__":
    file = open("midi_instruments.txt", "r")
    load_file(file)
    file.close()


dict = {
    "1": "",
    "2": ""
}