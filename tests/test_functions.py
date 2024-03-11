from src import functions


def test_is_executed():
    assert functions.is_executed({'state': 'EXECUTED'}) is True
    assert functions.is_executed({'state': 'CANCELED'}) is False


def test_get_date():
    assert functions.get_date({'date': '2018-12-06T21:34'})[:10] == '2018-12-06'


def test_get_description():
    assert functions.get_description({'description': "Открытие вклада"}) == "Открытие вклада"
    assert functions.get_description({'description': "Перевод организации"}) == "Перевод организации"
    assert functions.get_description({'description': "Перевод с карты на счет"}) == "Перевод с карты на счет"
    assert functions.get_description({'description': "Перевод с карты на карту"}) == "Перевод с карты на карту"
    assert functions.get_description({'description': "Перевод с карты на счет"}) != "Перевод с карты на карту"


def test_operation_from():
    assert functions.operation_from({'from': "MasterCard 3152479541115065"}) == "MasterCard 3152 47** **** 5065"
    assert functions.operation_from({'from': "Счет 75106830613657916952"}) == "Счет 7510 68** **** 6952"


def test_operation_to():
    assert functions.operation_to({'to': "Счет 11776614605963066702"}) == "Счет **6702"


def test_get_operationamount():
    assert functions.get_operationamount(
        {"operationAmount": {
                 "amount": "70946.18", "currency":
                 {"name": "USD", "code": "USD"}}
         }) == "70946.18 USD"


def test_print_operation():
    assert ((functions.print_operation(
        {'id': 441945886, 'state':
            'EXECUTED', 'date':
            '2019-08-26T10:50:58.294041', 'operationAmount': {
                                          'amount':
                                              '31957.58', 'currency':
                                          {
                                              'name':
                                                  'руб.', 'code':
                                              'RUB'}}, 'description':
            'Перевод организации', 'from':
            'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'})) ==
            '2019-08-26 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.')

