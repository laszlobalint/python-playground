def sport_intro(dictionary): 
  for key, val in dictionary.items():
    print(f'I chose {key}, and it is played in {val} form.')

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

sport_intro(equipment)
