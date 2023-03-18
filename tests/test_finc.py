from scr.finc import mask_account_number
from scr.finc import input_to
from scr.finc import datatime
from scr.finc import sorting_from_empty
from scr.finc import sorting_from_data

def test_mask_account_number():
    assert mask_account_number({"to": "Счет 64686473678894779589"}) == "Счет **9589"
    assert mask_account_number({"to": "Visa Platinum 8990922113665229"}) == "Visa Platinum 8990 09** **** 5229"

def test_input_to():
    assert input_to({"from": "Visa Classic 6831982476737658"}) == "Visa Classic 6831 19** **** 7658"
    assert input_to({"from": "Счет 48894435694657014368"}) == "Счет **4368"
    assert input_to({}) == "Выполнен перевод на счет вклада"

def test_datatime():
    assert datatime("2019-03-23T01:09:46.296404") == "23.3.2019"


def test_sorting_from_empty():
    assert sorting_from_empty([]) == []
    assert sorting_from_empty([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]

def test_sorting_from_data():
    assert sorting_from_data([{"date": "2019-08-26T10:50:58.294041"},{"date": "2019-07-03T18:35:29.512364"} ]) == [{'date': '2019-08-26T10:50:58.294041'}, {'date': '2019-07-03T18:35:29.512364'}]
    assert sorting_from_data([{"date": "2019-07-26T10:50:58.294041"},{"date": "2019-08-03T18:35:29.512364"}]) == [{'date': '2019-08-03T18:35:29.512364'}, {'date': '2019-07-26T10:50:58.294041'}]
