import json
from datetime import datetime
def load_file():
    """ функция преобразовывает файл json  в формат Python"""
    new_lines = []
    with open("operations.json", 'r', encoding='utf-8') as f:
        data_new = json.loads(f.read())

        return data_new

data = load_file()
print(data)

data.sort(key=lambda x: x['date'])
print(data)

#for i in load_file():
#    print(i['date'])
#    i['date'] = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f')
#    print(i)

