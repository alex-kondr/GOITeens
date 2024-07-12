transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}
for auto_number in transport:
    print(auto_number)

for auto_number in transport.keys():
    print(auto_number)

for full_name in transport.values():
    print(full_name)

for auto_number, full_name in transport.items():
    print(f"Власник Автомобіля з номерним знаком {auto_number} - {full_name}")