from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from itertools import groupby


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

PHONE_TEMP = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'

new_list = []
for item in contacts_list:
    full_name = ' '.join(item[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
              re.sub(PHONE_TEMP, PHONE_SUB, item[5]), item[6]]
    new_list.append(result)

list_norepeat = []
list_norepeat.append(new_list[0])
data_list = new_list[1:]
key_item = lambda x:x[:2]
data_list = sorted(data_list, key=key_item)
for key, group in groupby(data_list, key=key_item):
    new_row = ['','','','','','','']
    for row in group:
        i = 0
        for data in row:
            if new_row[i] == '' and data != '':
                new_row[i] = data
            i += 1
    list_norepeat.append(new_row)
pprint(list_norepeat)

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(list_norepeat)