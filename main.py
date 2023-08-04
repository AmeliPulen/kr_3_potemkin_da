from settings import PATH_WITH_FIXTURES
from app.src.utils import get_all_operations, get_executed_operations, get_newer_five_operations, get_validate_data

# Получаем список всех операций из файла
operations = get_all_operations(PATH_WITH_FIXTURES)

# Выделяем только EXECUTED операции, фильтруем до пяти последних и сортируем по дате
ex_operations = get_executed_operations(operations)
five_operations = get_newer_five_operations(ex_operations)

# Выводим результат
for operation in five_operations:
    if operation:
        print(get_validate_data(operation))