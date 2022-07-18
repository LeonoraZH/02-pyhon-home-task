# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях, позиции задаются с клавиатуры через пробел

number = int(input('Введите число: '))
numbers = list(range(-number, number + 1))
print(numbers)
positions = input('Введите номера позиций через пробел: ')
new_positions = positions.split()

def multiply(positions: list, array: list):
  mult = 1
  for i in positions:
    mult *= array[int(i)] 
  return mult


print(multiply(new_positions, numbers))

