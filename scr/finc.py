def mask_account_number(account_number):
    """функция маскировки номера"""
    new = account_number["to"]
    len_s = len(new)
    if "Счет" in new:
        return new[0:len_s - 20] + '**' + new[-4:]
    else:
        return new[0:len_s - 12] + ' ' + new[len_s - 13:len_s - 11] + '** **** ' + new[-4:]