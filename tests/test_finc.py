from scr.finc import mask_account_number


def test_mask_account_number():
    assert mask_account_number({"to": "Счет 64686473678894779589"}) == "Счет **9589"
    assert mask_account_number({"to": "Visa Platinum 8990922113665229"}) == "Visa Platinum 8990 09** **** 5229"