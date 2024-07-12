transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}
for car_numb in transport:
    print(car_numb)

for car_numb in transport.keys():
   print(car_numb)

for full_name in transport.values():
   print(full_name)

for car_num, full_name in transport.items():
    print(f"Власник Автомобіля з номерним знаком {car_num} - {full_name}")

transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
    'AB0212KK': 'Семенов Андрій',
}

transport.update({'AA1321AA': 'Іванов Сергій'})
transport[]