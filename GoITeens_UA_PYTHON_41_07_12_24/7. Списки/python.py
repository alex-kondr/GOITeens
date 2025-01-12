products = ["Хліб", "Кава", "Печиво", "Сіль", "Цукор"]
[4, 4, 6, 4, 5]

counts = []
for product in products:
    count = 0
    for char in product:
        count += 1

    counts += [count]