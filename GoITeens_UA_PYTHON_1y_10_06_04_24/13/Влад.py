transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}

for avto_number in transport.keys():
    print(avto_number)

for owner in transport.values():
    print(owner)

for avto_number, owner in transport.items():
    print(f"{owner} власник авто з номерним знаком: {avto_number}")