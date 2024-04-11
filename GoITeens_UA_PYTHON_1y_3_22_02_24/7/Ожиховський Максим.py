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
    "5. Знайти номер тварини за ім'ям",                            # break
    "6. Видалити помилково додану тварину за ім'ям",
    "7. Видалити помилково додану тварину за номером",
    "8. Відсортувати список тварин за алфавітом",
    "9. Змінити кличку тварини",                        # Видалити та вставити на її місце іншу (animals.insert(0, animal))
    "10. Вийти з програми"
]


while True:

    print("Список команд:\n")
    for command in commands:
        print(command)

    command = input("\nВведіть номер команди-> ")

    if command == "1":

        print("Список тварин на лікуванні:")
        for i in range(len(animals)):
            print(f"{i + 1}. {animals[i]}")

        input("\nНатисніть Enter для продовження")

    elif command == "2":
        animals.append(input("Вкажіть ім'я тварини для прийняття на лікування-> "))

        print("Ваша тваринка успішно записана на лікування!")

        input("\nНатисніть Enter для продовження")

    elif command == "3":

        animal_cured = input("Вкажіть кличку тварини щоб забрати її з лікування-> ")

        if animal_cured not in animals:
            print(f"Тварини {animal_cured} немає в списку тварин.")
            input("\nНатисніть Enter для продовження")
            continue

        animals.remove(animal_cured)
        animals_cured.append(animal_cured)
        print("Ваша тваринка вилікувана та очікує вас!")

        input("\nНатисніть Enter для продовження")

    elif command == "4":

        if len(animals_cured) == 0: # if not animals_cured:
            print("Список вилікуваних тварин наразі пустий")
            continue

        print("Список усіх вилікуваних тварин:")
        for animal_cured in animals_cured:
            print(animal_cured)

        input("\nНатисніть Enter для продовження")

    elif command == "5":
        animal_indx = input("Введіть тваринку, номер якої хочете знайти: ") # animal = input("Введіть тваринку, номер якої хочете знайти: ")

        if animal_indx not in animals:
            print(f"Тварини {animal_indx} немає в списку тварин.")
            input("\nНатисніть Enter для продовження")
            continue

        animal_index = animals.index(animal_indx)
        print(f"Тварина {animal_indx} має номер {animal_index + 1}")

        input("\nНатисніть Enter для продовження")

    elif command == "6":
        animals.remove(input("Введіть ім'я тварини щоб відмінити запис на лікування-> ")) # помилковий запис -> відміна запису

        print("Помилковий запис на лікування відмінено!") #

        input("\nНатисніть Enter для продовження")

    elif command == "7":
        animals.pop(int(input("Введіть номер тварини щоб відмінити запис на лікування-> ")) - 1) # немає перевірки

        print("Помилковий запис тварини на лікування відмінено!")

        input("\nНатисніть Enter для продовження")

    elif command == "8":
        animals_copy = animals.copy()
        animals_copy.sort()

        print("Список тварин на лікування за алфавітом:")

        for animal in animals_copy:
            print(animal)

        input("\nНатисніть Enter для продовження")

    elif command == "9":
        animal = input("Вкажіть ім'я тваринки яке хочете замінити-> ")
        new_animal_name = input("Введіть нове ім'я тварини-> ")

        animal_indx = animals.index(animal)

        animals.remove(animal)

        animals.insert(animal_indx, new_animal_name)
        print(f"Ім'я вказаної тварини змінилося на {new_animal_name}!")

        input("\nНатисніть Enter для продовження")

    elif command == "10":
        print("Дякуємо що звернулися до нашої клініки!") #
        break

