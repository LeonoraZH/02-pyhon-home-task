# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Enter a number: ')
def summ(text: str):
  summ = 0
  for item in text:
    if item.isdigit():
      summ += int(item)
  return summ

print(summ(number))
