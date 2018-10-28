def greet():
  print('Hello World!')

greet()


def greeting(name = 'Anonymus', time = 'all day'):
  print(f'Good {time}, {name}! Have a nice day!')

name = input('Enter your name: ')
time = input('Enter the of day: ')

greeting(name, time)
greeting()


def area(radius):
  return 3.142 * radius * radius

def vol(area, length):
  print(area * length)

radius = int(input('Enter a radius for circle: '))
length = int(input('Enter a length: '))

vol(area(radius), length)
