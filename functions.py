import json


def load_operations():
    """
    Загружает список операций из файла
    """
    with open('operations.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def is_executed(operation):
    return operation.get('state') == 'EXECUTED'


def date_order(operation):
    return operation.get('date')


def print_operation(operation):
    return f"{operation.get('state')} {operation.get('date')[:10]} **{operation.get('from', '*********')[5:6]}"
