# Козловцев Сергей
# Задача - 1
class TownCar:
    def __init__(self):
        self._speed = '80'
        self._color = 'green'
        self._name = ''
        self._is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(diraction):
        print('машина повернула',diraction)
class SportCar(TownCar):
    def __init__(self):
        self._speed = '120'
        self._color = 'red'
        self._name = ''
        self._is_police = False
class WorkCar(TownCar):
    def __init__(self):
        self._speed = '70'
        self._color = 'grey'
        self._name = ''
        self._is_police = False
class PoliceCar(TownCar):
    def __init__(self):
        self._speed = '120'
        self._color = 'white'
        self._name = ''
        self._is_police = True

# Задача - 1
class Person:
    def __init__(self):
        self.health = 100
        self.damage = 70
        self.armor = 50
class Player(Person):
    def attack(self):
        Enemy.health = Enemy.health - (Player.damage - Enemy.armor)
class Enemy(Person):
    def attack(self):
        Player.health = Player.health - (Enemy.damage - Player.armor)
