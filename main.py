# # Zadanie 1 #
#
# a = [1 - x for x in range(1,11)]
# print(a)
#
# b = [4 ** x for x in range(0,8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 2 #
#
# import random
# listy1 = [random.randint(1, 100) for _ in range(10)]
# listy2 = [x for x in listy1 if x % 2 == 0]
# print(listy2)
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 3 #
#
# slownik = {'mleko': '1', 'mąka': 'kg', 'jajka': 'sztuki'}
# print(slownik)
#
# slownik2 = {key: value for value, key in slownik.items()}
# print(slownik2)
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 4 #
#
# def check(a, b, c):
#     if a == b == c:
#         return 'Trójkąt równoboczny'
#     if a >= b and a >= c:
#         if a * 2 == b * 2 + c ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif b >= a and b >= c:
#         if b * 2 == a * 2 + c ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     else:
#         if c * 2 == b * 2 + a ** 2:
#             return 'Trójkąt prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#
#
# print(check(5, 4, 3))
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 5 #
#
# def polet(a=2, b=4, h=6):
#     return ((a + b) * h) / 2
#
# print(polet())
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 6 #
#
# def iloczyn(a = 1,q = 4, n = 10):
#     an = a*q
#     el = [a,an]
#     iloczyn = a*an
#     for x in range (3, n+1, 1):
#         wyr = a * q
#         el.insert(x, wyr)
#         an = wyr
#         iloczyn *= wyr
#     return iloczyn, el
# print(iloczyn(1, 2, 10))
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 7 #
#
# def funkcja(*liczba):
#     if len(liczba) != 3:
#         print('Błąd!!! Podaj tylko trzy liczby')
#
#     for element in range(liczba[0], liczba[1]):
#         print(element * liczba[1])
#
# funkcja(1,3,4)
#
# znakiod = "-------------------------------------"
# print(znakiod)
#
# # Zadanie 8 #
#
# def sklep(** produkty):
#     ilosc = len(produkty)
#     print("Produktow jest :", ilosc)
#     if ilosc == 0:
#         print("brak zakupow")
#     else:
#         if ilosc != 0 :
#             sum = 0
#             for price in produkty.values():
#                 sum+=price
#         return sum
# print(sklep(jablka = 2, ser = 3, chleb =1 ))
