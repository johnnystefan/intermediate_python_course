def run():

  super_dict = {
    "number_naturals": [1, 2, 3, 4, 5],
    "number_negative": [-1, -2, 3]
  }

  super_list = [
    1,
    {"number_naturals": [1, 2, 3, 4, 5], "number_negative": [-1, -2, 3]}]
  pass

  for value in super_list:
    print("-", value)

if __name__ == '__main__':
  run()