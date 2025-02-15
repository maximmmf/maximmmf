import random


class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} поїв! Голод: {self.hunger}")

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        print(f"{self.name} погрався! Щастя: {self.happiness}")


class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.knowledge = 50
        self.energy = 50
        self.motivation = 50

    def work(self):
        self.money += 30
        self.energy -= 15
        self.motivation -= 5
        print(f"{self.name} попрацював. Гроші: {self.money}, Енергія: {self.energy}, Мотивація: {self.motivation}")

    def study(self):
        if self.energy > 10 and self.motivation > 10:
            self.knowledge += 15
            self.energy -= 10
            self.motivation -= 5
            print(f"{self.name} вчився. Знання: {self.knowledge}, Енергія: {self.energy}, Мотивація: {self.motivation}")
        else:
            print(f"{self.name} занадто втомлений або не має мотивації, щоб вчитися!")

    def rest(self):
        if self.money >= 15:
            self.energy += 25
            self.money -= 15
            self.motivation += 10
            print(f"{self.name} відпочив. Енергія: {self.energy}, Гроші: {self.money}, Мотивація: {self.motivation}")
        else:
            print(f"{self.name} не має грошей на відпочинок!")

    def live_year(self):
        for day in range(1, 366):
            print(f"День {day}")
            if self.money < 15:
                self.work()
            elif self.energy < 20:
                self.rest()
            elif self.knowledge < 120:
                self.study()
            elif self.motivation < 20:
                self.rest()
            else:
                print(f"{self.name} добре справляється!")


student = Student("Олексій")
student.live_year()