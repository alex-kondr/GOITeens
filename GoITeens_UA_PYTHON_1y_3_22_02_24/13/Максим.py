
# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.
math_scores = {
    "Олександр": [8, 9, 7, 9, 6],
    "Андрій": [10, 7, 9, 10, 10],
    "Олег": [6, 7, 6, 9, 6]
}
 
student = input("Введіть імя студента, щоб дізнатися його середній бал\n->" )
student_scores = math_scores.get(student, [0])

average_evaluation = sum(student_scores) / len(student_scores)
print(f"Середній бал студента {student} = {average_evaluation} балів")


