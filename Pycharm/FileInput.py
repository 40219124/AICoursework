import os


class FileInput:

    def __init__(self):
        self.file_data = ""
        self.count = 0
        self.numbers = []
        self.read_file()
        self.process_data()
        self.print_file()

    def read_file(self):
        this_dir = os.path.dirname(__file__)
        rel_path = "..\Caverns\input1.cav"
        abs_path = os.path.join(this_dir, rel_path)
        with open(abs_path, 'r') as f:
            self.file_data = f.read()

    def process_data(self):
        sep = self.file_data.split(',')
        self.count = int(sep[0])
        for val in sep:
            self.numbers.append(int(val))

    def print_file(self):
        self.process_data()
        print(self.numbers[:1])
        print(self.numbers[1:1 + self.count * 2])
        for i in range(self.count):
            print(self.numbers[1 + self.count * 2 + self.count * i:1 + self.count * 2 + self.count * (i+1)])
