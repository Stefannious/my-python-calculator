def square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    return base ** exp
# новая функция
def cube(n):
    return n ** 3