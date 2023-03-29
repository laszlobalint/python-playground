def sport_type_count(dictionary):
  types = list(dictionary.values())
  for type in set(types):
    num = types.count(type)
    print(f'There are {num} {type} types.')

equipment = {}

while True:
  sport_name = input('Enter a type of sport: ')
  sport_form = input('Enter the form of that sport: ')
  equipment[sport_name] = sport_form

  another = input('Add another? (y/n) ')
  if another == 'y':
    continue
  else:
    break

sport_type_count(equipment)
