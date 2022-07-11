import csv
import re
from collections import defaultdict
from pprint import pprint

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

data = defaultdict(list)
contacts_list_rev = [contacts_list[0]]
pattern_person = r'[А-ЯЁ][а-яё]+'
pattern_phone = r'(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(\s*[а-я]*\.*)\s*(\d+)*\)*'
for elem in contacts_list[1:]:
    repair_person = re.findall(pattern_person, ''.join(elem[:3]))
    elem[-2] = re.sub(pattern_phone, r'+7(\2)\3-\4-\5 \6\7', elem[-2])
    try:
        elem[0] = repair_person[0]
        elem[1] = repair_person[1]
        elem[2] = repair_person[2]
    except IndexError:
        repair_person.append('')
# 3. объединить все дублирующиеся записи о человеке в одну.
count = 0
dict_person = defaultdict(list)
for info in contacts_list[1:]:
    key = tuple(info[:2])
    for index, item in enumerate(info):
        if item not in dict_person[key]:
            dict_person[key].insert(index, item)
contacts_list_rev.extend(list(dict_person.values()))
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_rev)
