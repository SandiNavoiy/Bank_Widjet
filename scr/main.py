from finc import sorting_from_empty, load_file, sorting_from_data, print_to_sum, print_from_to, \
    print_date_description

print("Последние 5  проведенных операций по Вашей карте:")

for i in range(5):
    transaction = sorting_from_data(sorting_from_empty(load_file("operations.json")))[i]
    print(f"{print_date_description(transaction)} \n"
          f"{print_from_to(transaction)} \n"
          f"{print_to_sum(transaction)}\n"
          f"_____________________")

# 8.12.2019 863064926 EXECUTED
# 7.12.2019 114832369 EXECUTED
# 19.11.2019 154927927 EXECUTED
# 13.11.2019 482520625 EXECUTED
# 5.11.2019 801684332 EXECUTED
