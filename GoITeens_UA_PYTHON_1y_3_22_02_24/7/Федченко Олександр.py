animals = [ 
    "Кілер" , 
    "Катран" , 
    "Крістіан" , 
 "Кербер" , 
    "Дарлінг" , 
    "Рефлект" , 
    "Фарадей" , 
    "Діксон" , 
    "Арнольд" , 
    "Парнас" 
] 
 
animals_cured = [] 
 
commands = [ 
    "1. Показати список тварин на лікуванні",         # print(animals) 
    "2. Додати нову тварину до списку на лікування",  # animals.append(animal) 
    "3. Тварину вилікувано",                          # animals.remove(animal), animals_cured.append(animal) 
    "4. Показати список вилікуваних тварин",          # print(animals_cured) 
    "5. Вийти з програми",                            # break 
    "6. Видалити помилково додану тварину за ім'ям", 
    "7. Видалити помилково додану тварину за номером", 
    "8. Відсортувати список тварин за ім'ям", 
    "9. Змінити ім'я тварини",                        # Видалити та вставити на її місце іншу (animals.insert(0, animal)) 
    "10. Знайти номер тварини за ім'ям"
]
while True: 
    print ()
    for command in commands:
        print(command)
        
    command = input("Введіть номер команди: ")
    
    if command == "1":
        for i in range(len(animals)):
            print(f"{i + 1}. {animals[i]}")
            
        input("\nНатисніть ʼEnter’ для продовження ")
    
    elif command == "2":
        animal = input("Введіть нову домашню тварину для додавання у список на лікування: ")
        if animal in animals: 
            input("\nТака тварина вже є у списку. Натисніть ‘Enter’ для продовження ")
            continue
        animals.append(animal)
        print(f"Тварина '{animal}' додана до списку ")
        input("\nНатисніть ʼEnter’ для продовження ")
    
    elif command == "3":
        animal = input("Введіть тварину яку ви хочете вилікувати: ")
        
        if animal in animals:
            animals.remove(animal)
            animals_cured.append(animal)
            print(f"\nТварину '{animal}'  вилікувано. Натисніть ʼEnter’ для продовження ")
        else:
            input("\nТакої тварини немає у списку. Натисніть ʼEnter’ для продовження ")
    
    elif command == "4":
        if not animals_cured:
            print("Список вилікуваних тварин пустий")
            
        for animal in animals_cured:
            print(animal)
            
            input("\nНатисніть ʼEnter’ для продовження ")
    
    elif command == "5":
        print("Бажаємо вам гарногодня,бувай!")
        break
    
    elif command == "6":
        animal = input("Введіть ім'я тварини, яку ви хочете видалити зі списку: ")
        if animal in animals:
            animals.remove(animal)
            input(f"\nТварину '{animal}' видалено зі списку. Натисніть ‘Enter’ для продовження ")
        else:
            input("\nТакої тварини немає у списку. Натисніть ‘Enter’ для продовження")
    
    elif command == "7":
        index = input("Введіть номер тварини, яку ви хочете видалити зі списку: ")
        if index and index.isdigit() and 0 < int(index) <= len(animals):
            animal = animals.pop(int(index) - 1)
            input(f"\nТварину '{animal}' видалено зі списку. Натисніть ‘Enter’ для продовження ")
        else:
            input("Ви ввели не вірний номер тварини. Натисніть ‘Enter’ для продовження ")
    
    elif command == "8":
        anm = sorted(animals)
        for animal in anm:
            print(animal)
            
            input("\nНатисніть ‘Enter’ для продовження")
    
    elif command == "9":
        animal = input("Змінити ім'я тварині: ")
        
        if animal in animals:
                    animal_new = input("Введіть нове ім'я для тварини: ") # Зменшити на два рівні вкладеності
                    idx = animals.index(animal)
                    animals.remove(animal)
                    animals.insert(idx, animal_new)
                    
                    input(f"Тваринку '{animal}' було змінено на '{animal_new}'. Натисніть ‘Enter’ для продовження ")
    
    elif command == "10":
        animal = input("Введіть ім'я тварини для її пошуку: ")
        
        if animal in animals:
            index = animals.index(animal)
            input(f"Тварина '{animal}' знаходиться за номером {index + 1}. Натисніть ‘Enter’ для продовження")
        else:
            input("Такої тварини немає. Натисніть ‘Enter’ для продовження")