# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }

# for avto_number in transport.keys():
#     print(avto_number)

# for owner in transport.values():
#     print(owner)

# for avto_number, owner in transport.items():
#     print(f"{owner} власник авто з номерним знаком: {avto_number}")



# Погода. У словнику збережено інформацію про температуру в різних містах: ключами є назви міст,
# значеннями - температура. Розрахуйте середню температуру за вказаними містами

temperatures = {"Київ" : 36,
                "Львів" : 32,
                "Черкаси" : 30,
                "Одеса" : 33

}

city_count = 0
sum_temperatures = 0

for city, temp in temperatures.items():
    city_count += 1
    sum_temperatures += temp

arithmetic_mean_temperatures = sum_temperatures / city_count

print(f"Середня температура в даних містах України дорівнює = {arithmetic_mean_temperatures}")


# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.

students = {"коля" : [3, 5, 4, 5, 5, 4, 4],
            "василь" : [3, 2, 2, 1, 2, 3, 2],
            "петро" : [5, 5, 5, 5, 5, 4, 5],
            "олег" : [3, 3, 3, 2, 4, 4, 3],
            "ігорь" : [4, 5, 4, 5, 5, 5, 4]
}

student_mark = input("Введіть ім'я учня, оцінки якого ви хочете дізнатися-> ").lower()
arithmetic_mean_students_marks = students.get(student_mark, [0])
arithmetic_mean_marks = sum(arithmetic_mean_students_marks) / len(arithmetic_mean_students_marks)
print(f"Середня оцінка учня {student_mark} = {arithmetic_mean_marks}")