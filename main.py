from functions import (load_operations, is_executed, date_order, print_operation)

operations = load_operations()
print(operations)

operation = list(
    map(
        print_operation,
        filter(
            is_executed,
            sorted(
                filter(
                    lambda x: x.get('date') is not None, operations),
                key=date_order))))[:5]


print("\n".join(operation))
