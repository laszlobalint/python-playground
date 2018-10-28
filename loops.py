warriors = ['Superman', 'Batman', 'Flash', 'Donatello']

# Whole loop
for warrior in warriors:
  print(warrior)

# Partial loop
for warrior in warriors[1:3]:
  print(warrior)

# Searching loop
for warrior in warriors:
  if warrior == 'Flash':
    print(f'{warrior} - fast and powerful')
    break
  else:
    print(warrior)

# While loop
age = 25
num = 0

while num < age:
  if num == 0:
    num += 1
    continue
  if num % 2 == 0:
    print(num)
  if num > 10:
    break
  num += 1