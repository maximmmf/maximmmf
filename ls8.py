import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def simulation():

    logging.info("Симуляция запущена.")
    time.sleep(1)
    logging.info("Симуляция завершена.")

def timing_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнена за {execution_time:.6f} секунд")
        return result
    return wrapper

def error_logging_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Ошибка в {func.__name__}: {e}")
            return None
    return wrapper

@error_logging_decorator
def faulty_function():

    return 1 / 0 

@timing_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

if __name__ == "__main__":
    simulation()

    result = example_function(10**6)
    print("Результат:", result)

    faulty_function()