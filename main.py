import csv
import re
from collections import defaultdict

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# 1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
#    В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# 2. привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер,
#    формат будет такой: +7(999)999-99-99 доб.9999;

correct_list = []
data = defaultdict(list)
contacts_list_rev = []
pattern_person = r'[А-ЯЁ][а-яё]+'
pattern_phone = r'(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(\s*[а-я]*\.*)\s*(\d+)*\)*'
for elem in contacts_list[1:]:
    repair_person = re.findall(pattern_person, ''.join(elem[:3]))
    if elem[-2] != '':
        elem[-2] = re.sub(pattern_phone, r'+7(\2)\3-\4-\5 \6\7', elem[-2])
    correct_list.append(repair_person + elem[3:])

# 3. объединить все дублирующиеся записи о человеке в одну.

dict_person = defaultdict(list)
for info in correct_list:
    key = tuple(info[:2])
    for item in info:
        if item not in dict_person[key]:
            dict_person[key].append(item)
contacts_list_rev.extend(list(dict_person.values()))

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
# # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_rev)
