# Завдання 1 - Видалення дублікатів слів у рядку
# Імплементуйте функцію, яка приймає рядок тексту і повертає новий рядок, де всі дублікати слів видалені.

my_string = "Видалення дублікатів слів у дублікатів у рядку дублікатів у"

def remove_dubl(text: str) -> str:
    unique = set(text.split())
    return " ".join(unique)




def remove_dubl_list(text: str) -> str:
    unique_worlds = []

    for world in text.split():
        if world not in unique_worlds:
            unique_worlds.append(world)

    return " ".join(unique_worlds)

print(remove_dubl_list(my_string))

# Завдання 2 - Перевірка кількості цифр у рядку
# Напишіть функцію, яка рахує кількість цифр у заданому рядку.

new_string = input("Введіть рядок: ")
numbers = []
for char in new_string:
   if char.isnumeric():
      numbers.append(char)

count_numbers = len(numbers)
print(count_numbers)