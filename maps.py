from random import shuffle

def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# For loop method
for word in words:
  anagrams.append(jumble(word))
print(anagrams)

# Map method (map(method, data))
print(list(map(jumble, words)))


# Comprehension method
print( [ jumble(word) for word in words ] )
