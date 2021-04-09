# Файл с магическими методами:

import os.path
import tempfile
from random import randint

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.cursor = 0
        if os.path.exists(self.path_to_file) == False:
            file_out = open(self.path_to_file, 'w')
            file_out.close()

    def __add__(self, other):
        #создаем файл с уникальным адресом
        adress = os.path.join(tempfile.gettempdir(), ('file' + str(randint(0,999))))
        print('адрес файла', adress)
        # складываем тексты в файлах
        with open(self.path_to_file, 'r') as f_1:
            with open(other.path_to_file, 'r') as f_2:
                sum_f = f_1.read() + f_2.read()
        print('сумма тут:', sum_f)
        #записываем сумму в файл
        with open(adress, 'w') as f_3:
            f_3.write(sum_f)
        new_file = File(adress)
        print('тип файла', type(new_file))
        return new_file

    def __str__(self):
        return self.path_to_file

    def read(self):
        with open(self.path_to_file, 'r') as text_file:
            return text_file.read()

    def write(self, text_in):
        with open(self.path_to_file, 'w') as inf:
            return inf.write(text_in)

    def __iter__(self):
        return self

    def __next__ (self):
        with open(self.path_to_file, 'r') as f_t:
            f_t.seek(self.cursor)
            row = f_t.readline()
            if not row:
                self.cursor = 0
                raise StopIteration('EOF')
            self.cursor = f_t.tell()
            return row


