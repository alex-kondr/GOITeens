# Записати сторони трикутника, та знайти його площу
# S = sqrt(p(p-a)(p-b)(p-c))
# p = (a + b + c) / 2

# a = 3
# b = 4
# c = 5
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(type(p))
# print(f"Площа трикутника: {S} кв.см.")





# М'яч падає з висоти h. Знайти максимальну швидкість м'яча та за який час він упаде на землю.
# v = sqrt(2 * g * h)
# t = sqrt((2 * h) / g)
# g = 9.8
# h = 100
# v = (2 * g * h) ** .5
# t = ((2 * h) / g) ** .5
# print(f"Максимальна швидкість = {v}, а час = {t}")






# first_number = 45.3
# second_number = -96.1
# bool_type = (first_number < second_number) or (first_number < 0) or (second_number < 0)
# print(bool_type)




# Оголосити змінну “city”, в яку присвоїти назву міста.
CITY = "Odesa"

# Оголосити три змінні, одна з яких дорівнюватиме довільному числу. Друга - в двічі більше число, третя - з протилежним знаком до другої змінної.
a = 8
b = a * 2
c = -b


# Оголосити змінну - довжина ребра куба. Обчислити його об'єм і вивести на екран.
a = 97
V = a ** 3
# print(f"Об'єм куба дорвінює {V}")



# Оголосити змінні — сторони довільного шестикутника. Обчислити периметр шестикутника та вивести його на екран.
a = 4
b = 5
c = 6
d = 89
e = 97
f = 102
# P = a + b + c + d + e + f
# print(f"Периметр шестикутника {P} см")


# Оголосити змінні — площа круга. Визначити довжину кола та сторону вписаного правильного трикутника. Вивести на екран довжину кола та довжину сторони трикутника.
# R = sqrt(S / Pi)
# l = 2 * Pi * R
# a = R * sqrt(3)
Pi = 3.14
S = 36 * Pi
R = (S / Pi) ** 0.5
l = 2 * Pi * R
a = R * 3 ** 0.5
# print(f"Довжина кола = {l}\nСторона трикутника: {a}")



# Оголосити змінні — 4 кути (їхня градусна міра). Оголосити наступну змінну is_quad, аби отримати булеве значення чи являється дана фігура чотирикутником
a1 = 50
a2 = 140
a3 = 124 # 123
a4 = 47
is_quad = (a1 + a2 + a3 + a4) == 360
# print(is_quad)




# Автомобіль на першій половині часу їхав зі швидкістю 36 км/год, а на другій — зі швидкістю 88.8 км/год. Знайти середню швидкість на всьому шляху.
# Vc = (V1 + V2) / 2
# V1 = 36
# V2 = 88.8
# Vc = (V1 + V2) / 2
# print(f"Середня швидкість автомобіля дорівнює {Vc}")

# None!!!!!!!!!!!!!!
# bool
############
# bool(0)
# bool(1)
# bool("Hello")
# bool(" ")
# bool("")
# bool()
# bool( )

# print("dsgdsgd dsg dsgdfg dfgd fh dfh dhdfh\
#       saczxvxvxcvcx")
# print(""""
      
      
      
      
#       dsfsdaf
#       ds
#       f
#       ds
#       f
#       ds
#       fds
    #   """)

# Автомобіль на першій половині шляху їхав зі швидкістю 25.5 км/год, а на другій — зі швидкістю 101.3 км/год.
# Знайти середню швидкість на всьому шляху.
# Vc = (2 * V1 * V2) / (V1 + V2)
# V1 = 25.5
# V2 = 101.3
# Vc = (2 * V1 * V2) / (V1 + V2)
# print(f"Середня швидкість довівнює {Vc}")
# Vc = (V1 + V2) / 2
# print(f"Середнє арифметичне = {Vc}")












# Створити програму звертання до користувача, щоб він ввів довільний символ.
# Побудувати за його допомогою квадрат
# name = "Friend"
# symbol = input(f"Hello {name}: > ")
# symbol = symbol[0]
# print(f"{symbol}  [  ]       " * 5)
# print(f"{symbol}       {symbol}\n" * 3, end="")
# print(f"{symbol} " * 5)









# Створити програму обрахунку віку. Користувач вводить рікня і поточний рік.
# birth_year = int(input("Введіть рік народження > "))
# now_year = input("Введіть поточний рік > ")
# now_year = int(now_year)
# print(f"Мені {now_year - int(birth_year)} років")










# Дано змінні A, B, C, D.
# Змінити їх значення, перемістивши вміст A — в D , D — в C , C — в B, B - в A і
# вивести нові значення змінних A, B, C, D.
# A = 5
# B = 6
# C = B ########
# B = A
# A = C
# D = 7
# C = 8
# D, C , B, A = A, D, C, B

# T = None
# print("Hello", a, "   ")
# print(f"{name}")
# print("{name}  {age} {city}".format(age=age, name=name, city=city))


# Відомо, що X кг борошна коштує B гривень. Визначити, скільки коштує 1 кг та Y кг борошна.
# X = 50
# B = 500
# Y = 1000

# cost = B / X
# print(f"Ціна за кілограм борошна {cost}")
# summary = Y * cost
# print(f"{Y} кг борошна кошує {summary} грн.")





# Дана відстань L в кілометрах. Використовуючи операцію ділення націло,
# визначити кількість повних кіл з радіусом R, у метрах, яку необхідно пробігти на таку відстань.
# l = 2 * Pi * R
L = 100
R = 0.1
Pi = 3.14
l = 2 * Pi * R
N = L / l
print(f"Необхідно пробігти {N} кіл")




# Дано розмір файлу в мегабайтах. Використовуючи операцію ділення націло, знайти кількість повних гігабайт, які займає даний файл. (1 гігабайт = 1024 мегабайти).











# Дано тризначне число. Знайти суму та добуток його цифр.




# Нехай нам необхідно розрахувати послуги споживання електрики.
# У змінній rate у нас знаходиться тариф за електроенергію 1.68,
# а в змінній value — значення показання лічильника, задайте для неї розумне ціле число в кіловатах.
# Розрахуйте та помістіть у змінну payment рахунок за електрику.







# З початку доби пройшло N хвилин (N — ціле). Знайти кількість повних днів, місяців, років.







# Дано ціле число A. Перевірити істинність висловлювання: Число A є негативне.







# У змінній rate у нас знаходиться тариф за електроенергію — 1.68.
# Але тепер нам потрібно вести розрахунок денного та нічного тарифу.
# Нічний тариф розраховується як половина денного.
# У змінній value_day — денні показання лічильника, а в змінній value_night — нічні.
# Розрахуйте та помістіть у змінну payment рахунок за електрику, але вже з урахуванням денного та нічного тарифів.






# Створити дві змінні first_name, яка містить ім'я, та last_name, в яку помістити прізвище.
# Давайте зробимо конкатенацію цих двох змінних через символ пробілу і помістимо результат у змінну full_name.




# На цю мить у нас є три змінні: first_name, last_name та full_name
# Додамо змінну message, яка фактично буде прототипом шаблонного листа користувачеві, який купив квиток.
# Цю змінну ми сформуємо за допомогою f-рядка.
# У змінну message ми, за допомогою f-рядка, помістимо рядок наступного змісту:
# "Dear <підставляємо first_name>, we inform you that you have purchased a ticket to travel to the island of Mauritius.
# Departure June 31 of this year. Have a passport at <підставляємо full_name>. We are looking forward to seeing you!"




# Перша змінна a дорівнює -2 + 3j і друга змінна b дорівнює 4 + 2.1j.
# Результат додавання необхідно помістити у змінну result.




# Необхідно обчислити корені квадратного рівняння.
# a · x2 + b · x + c = 0
# Задайте змінні коефіцієнти a, b, c зі значеннями -2, 7, -6 відповідно
# Дискримінант рівняння помістіть у змінну D
# D = b^2 - 4 · a · c
# Корені рівняння помістіть у змінні x1 та x2, відповідно.
# x1 = (-b + D^0.5) / (2 · a)
# x2 = (-b - D^0.5) / (2 · a)




# Заведіть чотири змінні різного типу та надайте їм значення відповідного типу.
# name — рядкова змінна
# age — числова змінна
# is_active — булева змінна
# subscription — встановити значення None


