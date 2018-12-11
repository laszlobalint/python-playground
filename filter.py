grades = ['A', 'B', 'F', 'C', 'F', 'A']

def remove_fails(grade):
  return grade != 'F'

# Using filter method
print(list(filter(remove_fails, grades)))

# Using for loop method
filtered_grades = []
for grade in grades:
  if grade != 'F':
    filtered_grades.append(grade)
print(filtered_grades)

# Using commprehension method
print([ grade for grade in grades if grade != 'F' ])
