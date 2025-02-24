result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Число 'a' повинно бути не менше 'b'")
        if b > 100:
            raise IndexError("Число 'b' не повинно перевищувати 100")
        return a / b
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Помилка: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        key = int(key) 
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Помилка при обробці пари ({key}, {value}): {e}")

print(result)
