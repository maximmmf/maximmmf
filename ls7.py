class IterableGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for i in range(self.start, self.stop):
            yield i

iter_obj = IterableGenerator(1, 5)
for num in iter_obj:
    print(num)


import functools

def safe_calculator(func):
    @functools.wraps(func)
    def wrapper(expression):
        try:
            return func(expression)
        except (SyntaxError, ZeroDivisionError, TypeError, NameError) as e:
            return f"Помилка: {e}"
    return wrapper

@safe_calculator
def calculate(expression):
    return eval(expression)

print(calculate("10 + 20"))  # 30
print(calculate("10 / 0"))   # Помилка: division by zero
print(calculate("abc + 5"))  # Помилка: name 'abc' is not defined


import datetime

class StudentLifeSimulator:
    def __init__(self, start_day):
        self.current_day = start_day

    def __iter__(self):
        return self

    def __next__(self):
        self.current_day += datetime.timedelta(days=1)
        return f"Новий день: {self.current_day}"

student = StudentLifeSimulator(datetime.date(2025, 2, 24))
for _ in range(3):
    print(next(student))