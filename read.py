text_file = open('files/text.txt')

for line in text_file:
  print(line.rstrip())
text_file.seek(0)
lines = text_file.readlines()
print(lines)

# Read from and until given character
text_file.seek(50)
file_text = text_file.read(100)
print(file_text)

text_file.close()

# Different way with closing the file
def sequence_filter(line):
  return '>' not in line

with open('files/sequence.txt') as seq_file:
  lines = seq_file.readlines()
  print(list(filter(sequence_filter, lines)))
