import json
from datetime import datetime
def load_file():
    """ функция преобразовывает файл json  в формат Python"""
    new_lines = []
    with open("operations.json", 'r', encoding='utf-8') as f:
        data_new = json.loads(f.read())

        return data_new

data = load_file()
print(data[1])

data.sort(key=lambda x: x.get('id', 0))
data.pop(0) #чистим первый элемент , ибо он пустой
print(data)
data.sort(key=lambda x: x['date'],reverse=True)
print(data)

print("Последние 5 операций:")

for i in range(6):
     transaction = data[i]
     if "CANCELED" in transaction["state"]:
         continue
     else:
         date = transaction["date"]
         id = transaction["id"]
         state = transaction["state"]

         print(f'{date} {id} {state}')


