import json
import re



def load_operations():
    """
    Загружает список операций из файла
    """
    with open('operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def is_executed(operation):
    """
    Фунция возвращает операции со статусом 'EXECUTED'
    """
    return operation.get('state') == 'EXECUTED'


def get_date(operation):
    """
    Фунция получает дату операции
    """
    return operation.get('date')[:10]


def format_date(operation):
    """
    Фунция редактирует дату операции
    """
    date_string = (operation.get('date')[:10]).split('-')
    return ':'.join(date_string[::-1])


def get_description(operation):
    """
    Фунция возвращает описание операции
    """
    return operation.get('description')


def operation_from(operation):
    """
    Фунция возвращает откуда был сделан перевод
    отделяет тип карты от номера
    разбивает номер карты на блоки по 4 цифры
    определяем данные для отображения
    возвращем в нужном формате
    """
    transaction_from = operation.get('from', '')
    if transaction_from == "":
        return transaction_from
    else:
        operation_card = transaction_from[0:transaction_from.rfind(' ',)]
        card_number = transaction_from[transaction_from.rfind(' ',):]
        from_card = str(re.sub(r'.{4}', r'\g<0> ', card_number[:0:-1])[::-1])
        from_card_open_beg = from_card[:8]
        from_card_open_end = from_card[-5:]
        return f'{operation_card}{from_card_open_beg}** ****{from_card_open_end}'


def operation_to(operation):
    """
    Фунция возвращает куда был сделан перевод
    маскирует часть номера карты
    """
    transaction_to = operation.get('to', '')
    to_card = transaction_to[0:transaction_to.rfind(' ',)]
    card_number = transaction_to[transaction_to.rfind(' ', ):]
    to_card_open_end = card_number[-4:]
    return f'{to_card} **{to_card_open_end}'


def get_operationamount(operation):
    """
    Фунция возвращает сумму и валюту перевода
    """
    return f"{operation.get('operationAmount')['amount']} {(operation.get('operationAmount')['currency'])['name']}"


def print_operation(operation):
    return (f"{format_date(operation)} "
            f"{get_description(operation)}\n"
            f"{operation_from(operation)} -> {operation_to(operation)}\n"
            f"{get_operationamount(operation)}")
