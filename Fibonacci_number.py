# Курс Stepik.org: Алгоритмы: теория и практика. Методы.
# Задача на программирование: небольшое число Фибоначчи

def fib(n):
    if n <= 1:
        return 1
    else:
        mas = [0, 1]
        for i in range(1, n):
            x = mas[-1] + mas[-2]
            mas.append(x)
    return mas[-1]
