# correct formats...
import math
from typing import Optional


def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def calculate_square_root(number: float) -> float:
    return math.sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        root: Optional[str] = '0'
    else:
        root = calculate_square_root(your_number)
    return root


num1: int = 10
num2: int = 5

print('Сумма чисел: ', add_numbers(num1, num2))

your_num: float = calc(25.5)

print(f'Мы вычислили квадратный корень из введённого вами числа.'
      f' Это будет: {your_num}')
