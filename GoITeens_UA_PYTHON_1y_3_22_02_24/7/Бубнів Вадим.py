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
 ]


while True:
    for command in commands:
        print(command)

    command = int(input("Введіть номер команди: "))

    if command > 8: # Краще використати else
        input("немає такоі команди, введіть Enter для продоаження;")
    elif command == 1:
        for num, anim in enumerate(animals):
            print (f"{1 + num}. {anim}")
        input("введіть Enter для продоаження;")

    elif command == 2:
        anim = input("введіть кличку тварини яку хочете добавити:")
        animals.append(anim)
        print("Тварину додано")
        input("введіть Enter для продоаження;")

    elif command == 3:
        animal = input("Введіть назву тварини яку вилікували: ")
        if animal not in animals:
             print("нема такоі тварини в списку")

        else:
            print("Тваринку вилікувано") # Краще перенести нижче
            animals.remove(animal)
            animals_cured.append(animal)
        input("введіть Enter для продоаження;")

    elif command == 4:
        print(animals_cured)
        input("введіть Enter для продоаження;")

    elif command == 5:
        input("був радий працювати з вами! До зустрічі!")
        break

    elif command == 6:
        andel = input("Введіть ім'я тварини яку хочете видалити: ")
        if andel not in animals:
            print("нема такоі тварини в списку")
        else:
            animals.remove(andel)
            print ("Тварину успішно видалено")
        input("введіть Enter для продоаження;") # Enter
    elif command == 7:
        index = input("введіть номер тварини яку хочете видалити: ")
        if index and index.isdigit() and 0 < int(index) <= len(animals):
            animl = animals.pop(int(index) - 1)
            print(f"тваринку {animl} видалено")
        else:
            input("Ви ввели не вірний номер тварини.")
        input("введіть Enter для продоаження;")

    elif command == 8:
        sortanimals = sorted(animals)
        print (sortanimals)
        for sam in sortanimals:
            print (sam)
        input("введіть Enter для продоаження;")
