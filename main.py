import json
def load_professions():
    """ функция загружает список проффессий из файла"""
    new_lines = []
    with open("operations.json", 'r', encoding='utf-8') as f:
        data = json.loads(f.read())


        return data


print(load_professions())