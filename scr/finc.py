import json
from datetime import datetime

def mask_account_number(account_number):
    """функция маскировки номера"""
    new = account_number["to"]
    len_s = len(new)
    if "Счет" in new:
        return new[0:len_s - 20] + '**' + new[-4:]
    else:
        return new[0:len_s - 12] + ' ' + new[len_s - 13:len_s - 11] + '** **** ' + new[-4:]

def input_to(account_to):
    """функция вывода с какой карты или счета идет перевод"""
    if "from" in account_to:
        new = account_to['from']
        len_s = len(new)
        if "Счет" in new:
            return new[0:len_s - 20] + '**' + new[-4:]
        else:
            return new[0:len_s - 12] + ' ' + new[len_s - 13:len_s - 11] + '** **** ' + new[-4:]
    else:
        return "Выполнен перевод на счет вклада"

def datatime(text):
    """функция преодразования строки к виду число-месяц-год"""
    datetime_object = datetime.strptime(text, '%Y-%m-%dT%H:%M:%S.%f')
    return f"{datetime_object.day}.{datetime_object.month}.{datetime_object.year}"


def sorting_from_empty(list_from_file):
    """ удаление пустых значений и не выполненых операций"""
    list_from_file_new = []
    for i in list_from_file:

        if i.get('state') == 'EXECUTED':
            list_from_file_new.append(i)

    return list_from_file_new

def load_file(file_of_json):
    """ функция преобразовывает файл json  в формат Python"""
    with open(file_of_json, 'r', encoding='utf-8') as f:
        data_new = json.loads(f.read())

        return data_new

def sorting_from_data(list_from_file):
    """сортировка по дате"""
    list_from_file.sort(key=lambda x: x['date'], reverse=True)
    return list_from_file