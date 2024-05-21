
# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.
math_scores = {
    "Олександр": [8, 9, 7, 9, 6],
    "Андрій": [10, 7, 9, 10, 10],
    "Олег": [6, 7, 6, 9, 6]
}


mean = 0
num = 0
sum = 0
name = input("Введіть ім'я про яке хочете дізнатись середній бал")


student = math_scores.get(name, "такого імені немає")
if isinstance(student, list):
    for numbers in student:
        if isinstance(numbers, int):
            num += 1
            sum += numbers
    mean = sum / num
    print (mean)
else:
    print(student)
