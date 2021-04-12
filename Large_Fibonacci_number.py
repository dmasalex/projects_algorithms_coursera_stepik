# Курс Stepik.org: Алгоритмы: теория и практика. Методы.
# Задача на программирование: последняя цифра большого числа Фибоначчи

def fib_digit(n):
    if n <= 1:
        return 1
    else:
        mas= [0, 1]
        for i in range(1, n):
            x = int(mas[-1]) + int(mas[-2])
            x = str(x)
            mas.append(x[-1])
            del mas[0]
    return mas[-1][-1]
