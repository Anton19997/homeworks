#Кожен пише суму списку за допомогою for та while
a = range(44)
x = 0
for i in range(len(a)):
    x += a[i]
print(x)



a = [1, 2, 3, 4, 5]
x = 0
i = 0
while i < len(a):
    x += a[i]
    i += 1
print(x)
#Банкомат видає суму максимально можливими купюрами

banknots = [1000, 500, 200, 100, 50, 20, 10]
suma = int(input("Cash"))
for i in range(len(banknots)):
    a = suma // banknots[i]
    suma = suma % banknots[i]
    if a > 0:
        print(banknots[i], a)

#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

banknots = [1000, 500, 200, 100, 50, 20, 10]
suma = int(input("Cash"))
counts = [10] * len(banknots)

for i in range(len(banknots)):
    if suma == 0:
        break
    elif suma < banknots[i]:
        continue
    else:
        count = min(suma // banknots[i], 10)
        counts[i] = count
        suma -= count * banknots[i]
        print(banknots[i], count)

#Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файла.
#Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані знання до виконання завдання.

with open('20Numb.txt', 'r') as file:
  lines = file.readlines()

def fizz_buzz(Fizz, Buzz, x):
  for i in range(1, x + 1):
      if i % Fizz == 0 and i % Buzz == 0:
          print("FB")
      elif i % Fizz == 0:
          print("F")
      elif i % Buzz == 0:
          print("B")
  return

for line in lines:
  Fizz, Buzz, End = map(int, line.split())
  fizz_buzz(Fizz, Buzz, End)