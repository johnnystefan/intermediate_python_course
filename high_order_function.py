def function_filter():

  #function FILTER
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

  odd = list(filter(lambda x: x % 2 != 0, my_list))

  print(odd)

def function_map():
  my_list = [1, 2, 3, 4, 5]

  squares = list(map(lambda x: x**2, my_list))

from functools import reduce

def function_reduce():
  my_list = [2, 2, 2, 2, 2]

  all_multiplied = reduce(lambda a, b: a * b, my_list)

  print(all_multiplied)


if __name__ == '__main__':
  function_reduce()