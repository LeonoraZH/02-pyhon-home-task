# Реализуйте алгоритм перемешивания списка.

import random


items = [65, 45, 12, 10, 2, 9, 71, 3]

def shuf(array: list):
  for i in range(0, len(array) - 1):
    index = random.randint(i, len(array) - 1)
    array[i], array[index] = array[index], array[i]
  return array

print(shuf(items))
