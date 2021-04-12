# Курс Stepik.org: Алгоритмы: теория и практика. Методы.
# Задача на программирование: наибольший общий делитель

def gcd(a, b):
    while True:
        if a == 0:
            print(b)
            break
        elif b == 0:
            print(a)
            break
        elif a >= b:
            return gcd(a % b, b)
        elif b >= a:
            return gcd(a, b % a)

gcd(14159572, 63967072)
