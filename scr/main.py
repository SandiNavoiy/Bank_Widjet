from finc import input_to
from finc import mask_account_number
from finc import datatime
from finc import sorting_from_empty
from finc import load_file
from finc import sorting_from_data


data_transaction = sorting_from_data(sorting_from_empty(load_file("operations.json")))
print("Последние 5  проведенных операций по Вашей карте:")

for i in range(5):
    transaction = data_transaction[i]
    print(f'{datatime(transaction["date"])} {transaction["description"]} ')
    print(f'{input_to(transaction)} -> {mask_account_number(transaction)}')
    print(f'{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]} ')


# 8.12.2019 863064926 EXECUTED
# 7.12.2019 114832369 EXECUTED
# 19.11.2019 154927927 EXECUTED
# 13.11.2019 482520625 EXECUTED
# 5.11.2019 801684332 EXECUTED
