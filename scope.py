name = 'Sam'

def print_name():
  global name
  name = 'Paulina'
  print('The name inside the function is', name)

print_name()

print('Outside the function the name is', name)
