"""
Описати функцію Even (K) логічного типу, яка повертає True, якщо цілий параметр K
є парним, і False в іншому випадку. З її допомогою знайти кількість парних чисел в
наборі з 10 цілих чисел.
"""
x = int(input("enter first number"))
k = list(range(x, x+10))


def even(k):
    count = 0
    for i in range(0, 10, 1):
        if k[i] % 2 == 0:
            count += 1
        i += 1
    print(count)
    return count


even(k)
