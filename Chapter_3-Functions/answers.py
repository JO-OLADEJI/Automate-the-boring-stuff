# The Collatz Sequence

def collatz(number):
  if number % 2 == 0:
    return number // 2
  else:
    return 3 * number + 1


def main():
  x = int(input('Enter an integer: '))

  done = False;
  while not done:
    value = collatz(x)
    print(value)

    if (value != 1):
      x = value
      continue
    else:
      done = True

main()



# The Collatz Sequence with Input Validation

def collatz(number):
  if number % 2 == 0:
    return number // 2
  else:
    return 3 * number + 1


def main():
  validated = False
  while not validated:
    raw_input = input('Enter an integer: ')

    try:
      x = int(raw_input)
      validated = True
    except:
      print('Invalid input! Enter an integer.')

  done = False;
  while not done:
    value = collatz(x)
    print(value)
    
    if (value != 1):
      x = value
      continue
    else:
      done = True

main()