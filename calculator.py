def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

if __name__ == "__main__":
    print("Калькулятор запущен")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 5 = {multiply(3, 5)}")
    print(f"10 / 2 = {divide(10, 2)}")
