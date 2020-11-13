#  1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
#  зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
#  (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
#  (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.color = (('red', 7), ('yellow', 2), ('green', 5))
    def running(self):
        for color, time in cycle(self.color):
            print(color, '(wait {} sec)'.format(time))
            sleep(time)


traffic_light = TrafficLight()
traffic_light.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.heigth = 5
    def asphalt(self):
        asphalt = self.length * self.width * self.weight * self.heigth / 1000
        print(f'result - {round(asphalt)} т')

my_road = Road(20, 5000)
my_road.asphalt()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus

pavel = Position('Pavel', 'Ivanov', 'Manager', {'wage': 100000, 'bonus': 30000})
print(pavel.get_full_name())
print(pavel.get_total_income())


#  4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
#  is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
#  остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
#  TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
#  должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is going'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}'.format(self.name, direction))

    def show_speed(self):
        print('Ваша скорость - ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Вы превысили скорость')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')


class PoliceCar(Car):
    pass


sport_car = SportCar(200, 'Красный', 'Ferrary', False)
town_car = TownCar(70, 'Серый', 'Nissan', False)
work_car = WorkCar(35, 'Черный', 'Mazda', False)
police_car = PoliceCar(89, 'Белый', 'Toyota', True)

sport_car.stop()
work_car.go()
town_car.show_speed()
police_car.turn('rigth')


#


#  5.  Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
#  и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
#  Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
#  классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
#  метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск зарисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()
pencil.draw()
handle.draw()

