#Задание №1
import os
import re
import csv

path = os.path.join(os.getcwd()+'\\'+'Less02\\')
file_lst = [path+'info_1.txt',path+'info_2.txt',path+'info_3.txt']
pattern = re.compile('^(Изготовитель системы|Название ОС|Код продукта|Тип системы):\s+(.+)')

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

def get_data(file_name,pattern):
    print(f'Передали файл {file_name}, с паттерном {pattern}')
    with open(file_name,'r') as f:
        for line in f.readlines():
            tmp = re.match(pattern, line)
            if tmp is not None:
                if tmp.group(1) == 'Название ОС':
                    os_name_list.append(tmp.group(2))
                elif tmp.group(1) == 'Код продукта':
                    os_code_list.append(tmp.group(2))
                elif tmp.group(1) == 'Изготовитель системы':
                    os_prod_list.append(tmp.group(2))
                elif tmp.group(1) == 'Тип системы':
                    os_type_list.append(tmp.group(2))
    main_data = [['Название ОС','Код продукта','Изготовитель системы','Тип системы']]
    for i in zip(os_name_list, os_code_list, os_prod_list, os_type_list):
        main_data.append(i)
    return main_data

def write_to_csv(res_file_name):
    print(res_file_name)
    for i in file_lst:
      main_data = get_data(i,pattern)

    print(main_data)
    with open(res_file_name,'w') as wfile:
        writer = csv.writer(wfile)
        writer.writerows(main_data)

write_to_csv(os.path.join(os.getcwd()+'\\'+'Less02\\')+input('Введите название файла для записи результатов: \n'))

#Задание №2
import json
import os

path = os.path.join(os.getcwd() + '\\' + 'Less02\\')


def write_order_to_json(item, quantity, price, buyer, date):

    all=[item, quantity, price, buyer, date]
    print(all)
    with open(path + 'orders.json', 'a') as wfile:
        json.dump(all,wfile, indent=4)

item = {'item': input(f'Введите значение item\n')}
quantity = {'quantity': input(f'Введите значение quantity\n')}
price = {'price': input(f'Введите значение price\n')}
buyer = {'buyer': input(f'Введите значение buyer\n')}
date = {'date': input(f'Введите значение date\n')}
write_order_to_json(item, quantity, price, buyer, date)


#Задание №3
import yaml
import os

path = os.path.join(os.getcwd() + '\\' + 'Less02\\')

def write_to_yaml(to_yaml):
    with open(path + 'file.yaml', 'w') as wfile:
        yaml.safe_dump(to_yaml, wfile, default_flow_style=True, allow_unicode=True)

def read_from_yaml():
    with open(path+'file.yaml', 'r') as rfile:
        return yaml.safe_load(rfile)


lst_1 = [1,2,3]
num_2 = 12345
dict_3 = {"val": "€"}
to_yaml = {'1': lst_1,'2': num_2,'3': dict_3}
write_to_yaml(to_yaml)
if read_from_yaml() == to_yaml:
    print('Оно совпадает!')