#//////1_Задача/////

# def distance(x1=0, y1=0, x2=0, y2=0):
#     dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
#     return dst
# res = distance(x1 = int(input('Введите х1:  ')), y1 = int(input('Введите y1:  ')), x2 = int(input('Введите х2:  ')), y2 = int(input('Введите y2:  ')))
# print(f'Ответ:  {res}')

#//////2_Задача/////

# def power(a = 0, n = 0):
#     res = 1
#     for i in range(n):
#         res = res * a
#     return res
# print(power(int(input('Введите число:  ')), int(input('Введите степень:  '))))

#//////3_Задача/////

# n = int(input('Введите число:  '))
# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))
# print(f'Число Фибоначчи:  {fib(n)}')

#//////4_Задача/////

# def is_year_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return (True)
#     else:
#         return (False)
# print(is_year_leap(int(input('Введите год:  '))))

#//////5_Задача/////

# def square(side):
#     return (f'Периметр: {side * 4} Площадь: {side ** 2} Диагональ: {side * 2 ** 0.5}')
# print(square(int(input('Введите сторону квадрата:  '))))

#//////6_Задача/////

# def season(month):
#     if month == 12 or 1 <= month <= 2:
#         return ('Зима')
#     elif 3 <= month <= 5:
#         return ('Весна')
#     elif 6 <= month <= 8:
#         return ('Лето')
#     elif 9 <= month <= 11:
#         return ('Осень')
#     else:
#         return ('Вы вели неправильный месяц')
# print(season(int(input('Введите номер месяца:  '))))

#//////7_Задача/////

# def bank(a, years):
#     for i in range(years):
#         a = a * 1.1
#     return a
# print(bank(int(input('Введите сумму вклада:  ')), int(input('На сколько лет:  '))))

#//////8_Задача/////

# def is_prime(n):
#     res = 0
#     if n >= 0 and n <= 1000:
#         for i in range(2, n // 2 + 1):
#             if (n % i == 0):
#                 res = res + 1
#         if (res <= 0):
#             return (True)
#         else:
#             return (False)
#     else:
#         return ('Вы ввели неправильное число')
# print(is_prime(int(input('Введите число от 0 до 1000:  '))))

#//////9_Задача/////

# def date(day, month, year):
#     days31 = [1, 3, 5, 7, 9, 11, 12]
#
#     if 1<= month <= 12 and 1<= year <=9999:
#         if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month==2 and day<=29:
#
#             return (True)
#         elif month==2 and day<=28:
#             return (True)
#         elif month in days31 and day<=31:
#             return  True
#         elif month not in days31 and day<=30:
#             return True
#         else:
#             return False
#     else:
#         return (False)
# print(date(int(input('Введите число:  ')), int(input('Введите месяц:  ')), int(input('Введите год:  '))))

