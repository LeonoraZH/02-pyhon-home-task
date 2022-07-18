# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


number = int(input('Enter a number: '))

def func(n: int):
  numbers = []
  summ = 0
  for i in range(1, n + 1):
    summ += (1 + 1/i) ** i
    numbers.append(summ)
  return numbers

print(func(number))
