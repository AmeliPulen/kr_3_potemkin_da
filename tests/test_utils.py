import pytest
from settings import PATH_WITH_FIXTURES
from app.src.utils import get_all_operations, get_executed_operations, get_newer_five_operations, convert_date, \
    convert_payment_info, get_validate_data


def test_get_all_operations():
    assert isinstance(get_all_operations(PATH_WITH_FIXTURES), list)
    with pytest.raises(FileNotFoundError):
        get_all_operations('asdasd')


def test_get_executed_operations(valid_data, one_executed_operation):
    assert len(get_executed_operations(valid_data)) == 6
    assert get_executed_operations(one_executed_operation) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


def test_get_newer_five_operations(newer_operation):
    assert get_newer_five_operations(newer_operation)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_convert_date():
    assert convert_date("2018-06-08T16:14:59.936274") == '08.06.2018'


def test_convert_payment_info():
    assert convert_payment_info("Visa Platinum 6942697754917688") == "Visa Platinum 6942 69** **** 7688"
    assert convert_payment_info("Счет 85458008326755993377") == "Счет **3377"


def test_get_validate_data(one_operation):
    assert get_validate_data(one_operation) == '06.09.2019 Перевод организации \nVisa Gold 3654 41** **** 1162 -> ' \
                                               'Счет **8289 \n6357.56 USD \n'
