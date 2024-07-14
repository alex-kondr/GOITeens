# Погода. У словнику збережено інформацію про температуру в різних містах: ключами є назви міст,
# значеннями - температура. Розрахуйте середню температуру за вказаними містами

#citys = {"Львів": 35,
#         "Київ": 33,
#         "Осло": 26,
#         "Оттава": 20
#         }


#city_count = 0
#temperature = 0

#for city in citys:
#    city_count += 1
#    temperature += citys[city]

#middle_temperature = temperature / city_count 

#print(f"Середня температура в цих містах: {middle_temperature}")




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

