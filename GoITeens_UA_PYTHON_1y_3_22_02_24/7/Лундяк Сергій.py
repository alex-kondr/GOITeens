animals = [
    "Кілер",
    "Катран",
    "Крістіан",
    "Кербер",
    "Дарлінг",
    "Рефлект",
    "Фарадей",
    "Діксон",
    "Арнольд",
    "Парнас"
]

animals_cured = []

commands = [
    "1. Показати список тварин на лікуванні",         # print(animals)
    "2. Додати нову тварину до списку на лікування",  # animals.append(animal)
    "3. Тварину вилікувано",                          # animals.remove(animal), animals_cured.append(animal)
    "4. Показати список вилікуваних тварин",          # print(animals_cured)
    "5. Вийти з програми",                            # break
#############################################################################################################
    "6. Видалити помилково додану тварину за ім'ям",
    "7. Видалити помилково додану тварину за номером",
    "8. Відсортувати список тварин за ім'ям",
    "9. Змінити ім'я тварини",                        # Видалити та вставити на її місце іншу (animals.insert(0, animal))
    "10. Знайти номер тварини за ім'ям"
]
while True:
    for command in commands:
        print(command)

    command = (input("Введіть номер команди "))

    if command == "1":
        for i, animals in enumerate(animals ,start = 1): # for i, animal in enumerate(animals ,start = 1):
            print(f"{i}.{animals}")
        input("n/ Натисніть 'Enter' для продовження ") # не вистачає enter
    elif command == "2":
        animal = (input("Введіть нову тварину "))
        if animal not in animals:
            animals.append(animal)
        input("n/ Натисніть 'Enter' для продовження ")
    elif command == "3":
        animal = (input("Введіть тварину яка вилікувана "))
        animals.remove(animal)
        animals_cured.append(animal)
    elif command == "4":
            print(f"{animals_cured}")
    elif command == "5":
        break











