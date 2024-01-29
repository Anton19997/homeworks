#Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру. Друга функція прийматиме рядок та приводитиме його до верхнього регістру.

#Головна програма має застосовувати обидві функції до списку рядків за допомогою map, для кожного з рядків, та друкувати результат.


s = str(input(""))
def s1(s):
    return s.lower()
a = list(map(s1, s))
print(a)
def s2(s):
    x = s.upper()
    return x
b = list(map(s2, s))
print(b)





#Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим. Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map
def one(y):
    return (y ** 2)
numbers = list(range(0, 50))
kvadrat = list(map(one, numbers))


def second(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

a = int(input("Enter a number: "))
print(second(a))
k = list(map(one, filter(second, numbers)))
print(k)

