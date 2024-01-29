#Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів). Знайти найуспішнішого і самого слабенького за середнім балом.
Python = {
    'Shtefan_Vika',
    "Gerasimov_Vasya",
    "Kuznetsov_Viktor",
    "Lastovetskiy_Vladimir"}

FrontEnd = {"Shestacov_Pavel", "Kozak_Yira", "Lastovetskiy_Vladimir"}
FullStack = {"Shteftan_Vika", "Kozak_Yira", "Ruban_Georgiy"}
Java = {"Kuznetsov_Viktor", "Ruban_Georgiy", "Kozak_Yira"}
Both_groups = Python & FrontEnd, FullStack, Java
print(Both_groups)
NOT_Frontend = (Python | Java | FullStack) - FrontEnd
print(NOT_Frontend)
Python_Java = Python | Java
print(Python_Java)  



#Створити структуру даних для студентів з імен та прізвищ, можна випадкових. Придумати структуру даних, щоб вказувати, у якій групі навчається студент (Групи Python, FrontEnd, FullStack, Java). Студент може навчатися у кількох групах. Потім вивести:
#студентів, які навчаються у двох та більше групах
#студентів, які не навчаються на фронтенді
#студентів, які вивчають Python або Java






a = {
    "Vasilev_Denis": [3, 5, 4, 3, 4],
    "Dorofeeva_Nady": [4, 5, 5, 4, 3], 
    "Dvornikov_Petya": [4, 4, 5, 4, 5],
    "Batanova_Alina": [5, 4, 3, 4, 5],
    "Kuznetsova_Anna": [3, 4, 4, 5, 4],}
print(a.keys())
GPA_Vasilev_Denis = sum(a["Vasilev_Denis"]) / len(a["Vasilev_Denis"])
GPA_Dorofeeva_Nady = sum(a["Dorofeeva_Nady" ]) / len(a["Dorofeeva_Nady"])
GPA_Dvornikov_Pety = sum(a["Dvornikov_Petya"]) / len(a["Dvornikov_Petya"])
GPA_Batanova_Alina = sum(a["Batanova_Alina"]) / len(a["Batanova_Alina"])
GPA_Kuznetsova_Anna = sum(a["Kuznetsova_Anna"]) / len(a["Kuznetsova_Anna"])
GPA = {
    "Vasilev_Denis": GPA_Vasilev_Denis,
    "Dorofoeva_Nady": GPA_Dorofeeva_Nady,
    "Dvornikov_Petya": GPA_Dvornikov_Pety,
    "Batanova_Alina": GPA_Batanova_Alina,
    "Kuznetsova_Anna": GPA_Kuznetsova_Anna}
print(GPA)
print(max(GPA.values()))
print(min(GPA.values()))


#Написати функцію переведення розмірів жіночої білизни з міжнародної у решту. Всередині функції потрібно просто звертатися до правильно складеного словника.


def size_international_to_regional(dict_size: dict, international_size: str, regional_id: str):
    output_size = dict_size[international_size][regional_id]
    return output_size


size = {
    'XXS': {'DE': 36, 'US': 8, 'FR': 38, 'UK': 24},
    'XS': {'DE': 38, 'US': 10, 'FR': 40, 'UK': 26},
    'S': {'DE': 40, 'US': 12, 'FR': 42, 'UK': 28},
    'M': {'DE': 42, 'US': 14, 'FR': 44, 'UK': 30},
    'L': {'DE': 44, 'US': 16, 'FR': 46, 'UK': 32},
    'XL': {'DE': 46, 'US': 18, 'FR': 48, 'UK': 34},
    'XXL': {'DE': 48, 'US': 20, 'FR': 50, 'UK': 36},
    'XXXL': {'DE': 50, 'US': 22, 'FR': 52, 'UK': 38},
}

# XL in US
print(size_international_to_regional(size, 'XL', 'US'))

# XXXL in DE
print(size_international_to_regional(size, 'XXXL', 'DE'))