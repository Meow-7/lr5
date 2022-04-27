"""
Описати функцію AddLeftDigit (D, K), що додає до цілого позитивного числа K
ліворуч цифру D (D - вхідний параметр цілого типу, що лежить в діапазоні 1-9, K -
параметр цілого типу, який є одночасно вхідним і вихідним). За допомогою цієї
функції послідовно додати до цього числа K ліворуч дані цифри D1 і D2, виводячи
результат кожного додавання.
"""
k = int(input("enter k: "))
d1 = int(input("enter d1: "))
d2 = 7
if d1 > 9 or d1 < 1 or k < 1:
    print("d must be from 1 to 9")
    exit(0)


def add_left_digit(d1, d2, k):
    k = int(str(d1) + str(k))
    print(k)
    k = int(str(d2) + str(k))
    print(k)


add_left_digit(d1, d2, k)
