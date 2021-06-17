def run():
  palidrome = lambda string: string == string[::-1]

  print(palidrome('HANNAH'))

if __name__ == '__main__':
  run()