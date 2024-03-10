# импортировали функции
from functions import (load_operations, is_executed, get_date, print_operation)

# загрузили список операций
operations = load_operations()

# используем map для применения функции к каждому элементу списка
# фильтруем список функцией is_executed и делаем защиту от пустых значений
# возвращем 5 операций, начиная с последней
operation = list(
    map(
        print_operation,
        filter(
            is_executed,
            sorted(
                filter(
                    lambda x: x.get('date') is not None, operations),
                key=get_date))))[:-6:-1]

# разделяем операции пустой строкой
print("\n\n".join(operation))
