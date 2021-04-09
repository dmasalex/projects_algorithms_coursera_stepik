# Задача 3 недели "Классы и наследование"

import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)


    def get_photo_file_ext(self):
        file_extension = os.path.splitext(self.photo_file_name)
        for i in file_extension:
            f_ext = i
        return f_ext



class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.body_whl = body_whl
        super().__init__(brand, photo_file_name, carrying)
        if self.body_whl == '':
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)
            self.body_whl = '0x0x0'
        else:
            zn = ''
            mas = []
            x = 'x'
            for i in self.body_whl:
                if i != x:
                    zn += i
                if i == x:
                    mas.append(zn)
                    zn = ''
            mas.append(zn)
            if len(mas) == 3:
                try:
                    self.body_length = float(mas[0])
                    self.body_width = float(mas[1])
                    self.body_height = float(mas[2])
                except ValueError:
                    self.body_length = float(0)
                    self.body_width = float(0)
                    self.body_height = float(0)
            else:
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(adr):
    car_list = []
    with open(adr) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if row != [] and row[0] != '' and row[1] != '' and row[3] != '' and row[5] != '': 
                car_list.append(row)
    mas = []
    for i in range(len(car_list)):
        if car_list[i][3] != '' and '.' in car_list[i][3]:
            mas.append(car_list[i])
    cars = []
    for i in range(len(mas)):
        f = os.path.splitext(mas[i][3])
        j_1, j_2, j_3, j_4 = '.jpg', '.jpeg', '.png', '.gif'
        if f[1] == j_1 or f[1] == j_2 or f[1] == j_3 or f[1] == j_4:
            cars.append(mas[i])
    car_list = []
    for i in range(len(cars)):
        c_1, c_2, c_3 = 'car', 'truck', 'spec_machine'
        if cars[i][0] == c_1 or cars[i][0] == c_2 or cars[i][0] == c_3:
            car_list.append(cars[i])
    for i, j in enumerate(car_list):
        if car_list[i][0] == 'car' and car_list[i][2] == '':
            del car_list[i]
    for i, j in enumerate(car_list):
        if car_list[i][0] == 'spec_machine' and car_list[i][6] == '':
            del car_list[i]
    cars = []
    for i in range(len(car_list)):
        if car_list[i][0] == 'car':
            car = Car(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][2])
            cars.append(car)
        if car_list[i][0] == 'truck':
            truck = Truck(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][4])
            cars.append(truck)
        if car_list[i][0] == 'spec_machine':
            spec_machine = SpecMachine(car_list[i][1], car_list[i][3], car_list[i][5], car_list[i][6])
            cars.append(spec_machine)
    return cars


# Проверка работоспособности:

car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
print(spec_machine.get_photo_file_ext())
cars = get_car_list('/Users/dmasalex/_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
print(cars)
print(len(cars))
for car in cars:
    print(type(car))
print(cars[0].passenger_seats_count)
print(cars[1].get_body_volume())
print(cars[0].car_type, cars[0].brand, cars[0].passenger_seats_count, cars[0].photo_file_name, cars[0].carrying)
print(cars[1].car_type, cars[1].brand, cars[1].photo_file_name, cars[1].body_whl, cars[1].carrying)
print(cars[2].car_type, cars[2].brand, cars[2].photo_file_name, cars[2].body_whl, cars[2].carrying)
print(cars[3].car_type, cars[3].brand, cars[3].passenger_seats_count, cars[3].photo_file_name, cars[3].carrying)
print(cars[4].car_type, cars[4].brand, cars[4].photo_file_name, cars[4].carrying, cars[4].extra)
print(cars[2].get_body_volume())




