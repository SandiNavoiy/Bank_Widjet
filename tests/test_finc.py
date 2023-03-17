from scr.finc import mask_account_number


def test_mask_account_number():
    assert mask_account_number({"to": "Счет 64686473678894779589"}) == "/lihlijli"