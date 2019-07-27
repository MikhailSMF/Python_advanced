# Задание №1
first = 'разработка'
second = 'сокет'
third = 'декоратор'

print(f'Тип первого слова: {type(first)}, содержит: {first}\n'\
      f'Тип второго слова: {type(second)}, содержит: {second}\n'\
      f'Тип третьего слова: {type(third)}, содержит: {third}\n')


print(f'Тип первого преобразованного: {type( first.encode())},содержит: { first.encode()}\n'\
      f'Тип второго преобразованного: {type( second.encode())},содержит: { second.encode()}\n'\
      f'Тип третьего преобразованного: {type( third.encode())},содержит: { third.encode()}\n')

# Задание №2
first = b'class'
second = b'function'
third = b'method'

print(f'Тип первого слова: {type(first)}, содержит: {first}, длина {len(first)}\n'\
      f'Тип второго слова: {type(second)}, содержит: {second}, длина {len(second)}\n'\
      f'Тип третьего слова: {type(third)}, содержит: {third}, длина {len(third)}\n')

# Задание №3
a = b'attribute'    #Можно записать
b = b'класс'        #Нельзя записать
c = b'функция'      #Нельзя записать
d = b'type'         #Можно записать

# Задание №4
lst = ['разработка','администрирование','protocol','standard']
lst_byte = []
lst_new = []
for i in lst:
    lst_byte.append(i.encode())
print(f'Байтовая строка из str: {lst_byte}')
for i in lst_byte:
    lst_new.append(i.decode())
print(f'Строковое представление из байтового: {lst_new}')

# Задание №5
import requests
lst_site = ['https://yandex.ru/','https://youtube.com/']
try:
    for i in lst_site:
        response = requests.get(i)
        print(f'Опрошенная страница: {i}')
        print(f'Возвращенный тип: {type(response.content)}')
        print(f'Исходный текст: {response.content}')
        print(f'Преобразованный тип: {type(response.content.decode())}')
        print(f'Преобразованный текст: {response.content.decode()}'[0:5000])
except Exception:
    print('ohhh Error')

# Задание №6
# Задание №5
import os
from chardet.universaldetector import UniversalDetector

text = ['сетевое программирование','сокет','декоратор']
path = os.path.join(os.getcwd()+'\\'+'test.txt')

with open(path, 'w') as f:
    for i in text:
        f.write(i+'\n')

detector = UniversalDetector() #взято c https://chardet.readthedocs.io/en/latest/usage.html
with open(path, 'rb') as f:
    for line in f.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(f'Текущая кодировка по умолчанию: {detector.result}')

print('Попытка открыть с кодировкой UTF-8')
try:
    with open(path,'r',encoding='UTF-8') as f:
        print(f.readlines())
except UnicodeError:
    print('Ошибка кодировки при открытии')