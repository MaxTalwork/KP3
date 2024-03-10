import json

def load_operations():
    """
    Загружает список операций из файла
    """
    with open('operations.json', 'r', encoding='utf-8') as f:
        file = f.read()
        operations = json.loads(file)
    return operations
