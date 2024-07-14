# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }
# for auto_number in transport:
#     print(auto_number)

# for auto_number in transport.keys():
#     print(auto_number)

# for full_name in transport.values():
#     print(full_name)

# for auto_number, full_name in transport.items():
#     print(f"Власник Автомобіля з номерним знаком {auto_number} - {full_name}")



# Погода. У словнику збережено інформацію про температуру в різних містах: ключами є назви міст,
# значеннями - температура. Розрахуйте середню температуру за вказаними містами

#
#city_count = 0
#city_temperatures = 0
#for city, temp in temperature.items():
#arithmetic_city_temperature = city_temperatures / city_count
#print(f"Середня температура в містах дорівнює: {arithmetic_city_temperature}")
 



# Створіть словник, який містить ключ — ім’я студента, значення — список із балами.
# Попросіть користувача ввести ім’я студента.
# Порахувати середній бал студента, ім’я якого ввів користувач.
students = {"коля" : [3, 5, 4, 5, 5, 4, 4],
            "василь" : [3, 2, 2, 1, 2, 3, 2],
            "петро" : [5, 5, 5, 5, 5, 4, 5],
            "олег" : [3, 3, 3, 2, 4, 4, 3],
            "ігорь" : [4, 5, 4, 5, 5, 5, 4]
}

sum_all_grades = 0
grades_count = 0

for grades in students.values():
    sum_all_grades += sum(grades)
    grades_count += len(grades)

avg = sum_all_grades / grades_count
print(f"Середня оцінка всіх студентів: {avg} б")