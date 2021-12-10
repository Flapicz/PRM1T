class PhoneBook:
    def __init__(self, id):
        self.id = id
        self.dictionary = {}

    def add_record(self, user, number):
        assert user and number != ''
        assert number.isdigit() is True
        self.dictionary[user] = number

    def show_records(self):
        print(self.dictionary)

    def read(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                #print(line)
                temp = line.split(',')
                temp[1] = temp[1].strip()
                book1.add_record(temp[0], temp[1])
        book1.show_records()

    def write(self,filename):
        with open(filename, 'w') as file:
            for entry in self.dictionary:
                file.write(f'{entry}, {self.dictionary[entry]} \n')


if __name__ == '__main__':
    try:
        book1 = PhoneBook('1')
        book1.add_record('user4', '123234456')
        book1.add_record('user5', '23879')
        book1.show_records()
        book1.add_record('', '000000')
        book1.show_records()
        book1.add_record('user5', 'user6')
        book1.read("test.txt")
        book1.write("writetest.txt")
    except AssertionError:
        print('Podano niepoprawna wartosc')
