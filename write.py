with open('files/write.txt', 'w') as write_file:
  write_file.write('Python is awesome and it is quite enjoyable.')

with open('files/write.txt', 'a') as write_file:
  write_file.write('\nI love it so much, I dream in Python.')

quotes = [
  '\nI\'m selfish, impatient and a little insecure.'
  '\nI make mistakes, I am out of control and at times hard to handle.'
  '\nBut if you can\'t handle me at my worst, then you sure as hell don\'t deserve me at my best.'
]

with open('files/write.txt', 'a') as write_file:
  write_file.writelines(quotes)
