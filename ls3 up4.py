import random

class Man:
    def __init__(self, name, level):
        self.name = name
        self.level = level  # 1 - первоклассник, 2 - второклассник
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
            print(f"{self.name} слишком устал или не замотивирован , чтобы учиться!")

    def rest(self):
        self.energy += 20
        self.motivation += 10
        print(f"{self.name} отдохнул. Энергия: {self.energy}, Мотивация: {self.motivation}")

    def talk(self, other):
        if isinstance(other, Man):
            print(
                f"{self.name} ({self.level} класс) говорит с {other.name} ({other.level} класс): \"Привет, как дела?\"")
            other.respond()

    def respond(self):
        responses = ["Все отлично!", "Устал немного...", "Учёба сложная, но справляюсь!"]
        print(f"{self.name}: {random.choice(responses)}")


student1 = Man("МАксим", 1)
student2 = Man("Денис", 1)

student1.talk(student2)
