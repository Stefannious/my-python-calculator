from calculator import add, multiply, divide, subtract
from utils import square, factorial, power

if __name__ == "__main__":
    print("=== Калькулятор ===")
    print(f"5 + 7 = {add(5, 7)}")
    print(f"10 - 3 = {subtract(10, 3)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"20 / 4 = {divide(20, 4)}")

    print("\n=== Утилиты ===")
    print(f"Квадрат 6 = {square(6)}")
    print(f"5! = {factorial(5)}")
    print(f"2^10 = {power(2, 10)}")
