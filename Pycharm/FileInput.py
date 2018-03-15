import os


class FileInput:

    file_data = ""
    count = 0
    numbers = []

    @staticmethod
    def do_file_input():
        FileInput.read_file()
        FileInput.process_data()
        FileInput.print_file()

    @staticmethod
    def read_file():
        this_dir = os.path.dirname(__file__)
        rel_path = "..\Caverns\input.cav"
        abs_path = os.path.join(this_dir, rel_path)
        with open(abs_path, 'r') as f:
            FileInput.file_data = f.read()

    @staticmethod
    def process_data():
        if len(FileInput.numbers) > 0:
            FileInput.numbers.clear()
        sep = FileInput.file_data.split(',')
        FileInput.count = int(sep[0])
        for val in sep:
            FileInput.numbers.append(int(val))

    @staticmethod
    def print_file():
        print(FileInput.numbers[:1])
        print(FileInput.numbers[1:1 + FileInput.count * 2])
        for i in range(FileInput.count):
            print(FileInput.numbers[1 + FileInput.count * 2 + FileInput.count * i:
                                    1 + FileInput.count * 2 + FileInput.count * (i+1)])
