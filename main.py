import json
from datetime import datetime
def load_file(file_of_json):
    """ функция преобразовывает файл json  в формат Python"""
    new_lines = []
    with open(file_of_json, 'r', encoding='utf-8') as f:
        data_new = json.loads(f.read())

        return data_new

def datatime(text):
    """функция преодразования строки к виду число-месяц-год"""
    datetime_object = datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%f')
    return f"{datetime_object.day}.{datetime_object.month}.{datetime_object.year}"

def sorting_from_empty(list_from_file):
    """ удаление пустых значений и не выполненых операций"""
    list_from_file_new = []
    for i in list_from_file:
        # Если имя текущего элемента равно 'Alice', добавляем его в новый список
        if i.get('state') == 'EXECUTED':
            list_from_file_new.append(i)

    return list_from_file_new

def sorting_from_data(list_from_file):
    """сортировка по дате"""
    list_from_file.sort(key=lambda x: x['date'], reverse=True)
    return list_from_file

data_transaction = sorting_from_data(sorting_from_empty(load_file("operations.json")))


print("Последние 5  проведенных операций по Вашей карте:")

for i in range(5):
     transaction = data_transaction[i]

     print(f'{datatime(transaction["date"])} {transaction["description"]} ')
     print(f'{transaction["to"]} -> {transaction["to"]}')
     print(f'{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]} ')
     print("-------------")

#8.12.2019 863064926 EXECUTED
#7.12.2019 114832369 EXECUTED
#19.11.2019 154927927 EXECUTED
#13.11.2019 482520625 EXECUTED
#5.11.2019 801684332 EXECUTED

