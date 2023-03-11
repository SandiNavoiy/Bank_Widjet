import json
def load_file():
    """ функция преобразовывает файл json  в формат Python"""
    new_lines = []
    with open("operations.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())


        return data

#print(load_file())

for i in load_file():
    print(i)
