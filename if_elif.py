age = int(input('Enter your age: '))

if age < 10:
  print('You are very young!')
elif age < 40:
  print('Golden years are still yet to come.')
else:
  print('You are wise beyond doubt.')


meaty = input('Do you eat meat? (y/n): ')

if meaty == 'y':
  print('Here is the normal meaty menu...')
else:
  print('Here is the vegetarian menu...')
  