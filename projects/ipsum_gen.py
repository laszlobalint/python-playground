from random import randint

ninja_words = [
  'assassin', 'shinobi', 'hidden warrior', 'spy', 'kunoichi', 'combatant', 'shadow', 'master', 'skibo', 'bump', 'night warrior'
]

def ninjarize(word):
  random_pos = randint(0, len(ninja_words) - 1)
  return f'{word} {ninja_words[random_pos]}'

paragraphs = int(input('How many paragraphs of ninja ipsum do you want? : '))

with open('ipsum.txt') as ipsum_original:
  items = ipsum_original.read().split()

  for n in range(paragraphs):
    ninja_text = list(map(ninjarize, items))
    with open('ninja_ipsum.txt', 'a') as ipsum_ninja:
      ipsum_ninja.write(' '.join(ninja_text) + '\n\n')
