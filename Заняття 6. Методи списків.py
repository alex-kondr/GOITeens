# pip install faker

import random
from faker import Faker

fake = Faker("uk_UA")

students = []

for _ in range(50):
    first_name = fake.first_name()
    middle_name = fake.middle_name()
    last_name = fake.last_name()

    students.append([first_name, middle_name, last_name])

print(students)

for student in students:
    if student[2].startswith("А"):
        print(student)

random.randint(15, 60)