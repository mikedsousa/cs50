# students = {
#   "Harry": "Gryffindor",
#   "Hermione": "Gryffindor",
#   "Ron": "Gryffindor",
#   "Draco": "Slytherin",
# }

# for student in students:
#   print(student, students[student], sep=" from house ")

###################################

# for student in students:
#     print(f"Welcome to Hogwarts, {student}!")
  
# for i in range(len(students)):
#   print(i + 1, students[i])

###################################

students = [
  {
    "name": "Harry",
    "house": "Gryffindor",
    "patronus": "Stag"
  },
  {
    "name": "Hermione",
    "house": "Gryffindor",
    "patronus": "Otter"
  },
  {
    "name": "Ron",
    "house": "Gryffindor",
    "patronus": "Jack Russell Terrier"
  },
  {
    "name": "Draco",
    "house": "Slytherin",
    "patronus": None
  },
]

for student in students:
  print(f"Welcome to Hogwarts, {student['name']} from house {student['house']}! Your patronus is a {student['patronus']}.")