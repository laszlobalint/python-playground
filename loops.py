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
