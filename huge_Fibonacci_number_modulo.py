# # Курс Stepik.org: Алгоритмы: теория и практика. Методы.
# Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

def fib_mod(n, m):
	if 1 <= n <= 10 ** 18 and 2 <= m <= 10 ** 5:
        mas = [0, 1]
        for i in range(1, n):
            x = (mas[-1] + mas[-2]) % m
            y = mas[-1] + x
            if x != 0 or y != 1:
                mas.append(x)
            else:
                break
        return mas[-1]

fib_mod(10, 2)

def fib(n, m):
    if 1 <= n <= 10 ** 18 and 2 <= m <= 10 ** 5:
        mas = [0, 1]
        for i in range(1, 6 * m + 2):
            x = (mas[-1] + mas[-2]) % m
            mas.append(x)
            if mas[-2] == 0 and mas[-1] == 1:
                break
        print(mas, len(mas)-2)
    if mas[-1] == 0 and mas[-2] == 0:
        print(mas[-3])
    else:
        print(mas[-1])

fib(999999999999999999, 8)
