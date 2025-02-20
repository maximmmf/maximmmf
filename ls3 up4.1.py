import random


class Man:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.energy = 50
        self.knowledge = 50
        self.motivation = 50

    def study(self):
        if self.energy > 10 and self.motivation > 10:
            self.knowledge += 15
            self.energy -= 10
            self.motivation -= 5
            print(f"{self.name} учится. Знания: {self.knowledge}, Энергия: {self.energy}, Мотивация: {self.motivation}")
        else:
            print(f"{self.name} слишком устал или не мотивирован, чтобы учиться!")

    def rest(self):
        self.energy += 20
        self.motivation += 10
        print(f"{self.name} отдохнул. Энергия: {self.energy}, Мотивация: {self.motivation}")

    def talk(self, other):
        if isinstance(other, Man):
            print(
                f"{self.name} ({self.level} класс) говорит с {other.name} ({other.level} класс): \"Привет как дела?\"")
            other.respond()

    def respond(self):
        responses = ["Все отлично!", "Устал немного", "Учёба сложная, но я справляюсь"]
        print(f"{self.name}: {random.choice(responses)}")


class FirstGrader(Man):
    def __init__(self, name):
        super().__init__(name, 1)
        self.favorite_toy = "Машинка"

    def play(self):
        print(f"{self.name} играет с любимой игрушкой: {self.favorite_toy}")


class SecondGrader(Man):
    def __init__(self, name):
        super().__init__(name, 2)
        self.favorite_subject = "Математика"

    def solve_problems(self):
        print(f"{self.name} решает задачи по {self.favorite_subject}")


student1 = FirstGrader("МАксим")
student2 = SecondGrader("Денис")

student1.talk(student2)
student1.play()
student2.solve_problems()
