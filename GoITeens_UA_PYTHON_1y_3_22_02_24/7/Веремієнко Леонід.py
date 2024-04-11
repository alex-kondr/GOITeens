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
]

while True:
    for command in commands:
        print(command)

    command = input("Введіть номер команди: ")

    if command == "1":
        for i, animals in enumerate(animals, start=1): # for i, animal in enumerate(animals, start=1):
            print(f"{i}. {animals}")

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "2":
        animal = input("Напишіть яку тварнику хочете полікувати (назву) \n >>")

        if animal not in animals:
            str(animals.append(animal)) # animals.append(animal)


        input("Список тварин на лікуванні розширено. Натисніть 'Enter' для продовження ")



    elif command == "3": # зайві enter
        animal = input("Яку тварину вилікували\n >>")
        animals_cured.append(animal)
        input("Список вилікуваних розширено. Натисніть 'Enter' для продовження ")


    elif command == "4": # зайві enter
        for i, animals_cured in enumerate(animals_cured, start=1): # for i, animal in enumerate(animals_cured, start=1):
            print(f"{i}. {animals_cured}") # print(f"{i}. {animal}")

        input("\nНатисніть 'Enter' для продовження ")

    elif command == "5":
        print("Дякую! допобачення!")
        break


