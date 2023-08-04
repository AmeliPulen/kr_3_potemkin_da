import datetime
import json


def get_all_operations(path: str) -> list[dict]:
    with open(path, 'r') as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    executed_operations = list()
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_newer_five_operations(executed_operations: list[dict]) -> list[dict]:
    return list(sorted(executed_operations, key=lambda operation: operation['date'], reverse=True))[:5]


def convert_date(date: str) -> str:
    date_ = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.datetime.strftime(date_, '%d.%m.%Y')


def convert_payment_info(info: str) -> str:
    if info.startswith('Счет'):
        return f'Счет **{info[-4:]}'
    else:
        return f'{info[:-17]} {info[-16:-12]} {info[-12:-10]}** **** {info[-4:]}'


def get_validate_data(operation: dict) -> str:
    date = convert_date(operation['date'])
    from_ = convert_payment_info(operation['from']) if operation.get('from') else 'Внесение наличных'
    to_ = convert_payment_info(operation['to'])
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["name"]
    return f'{date} {operation["description"]} \n{from_} -> {to_} \n{amount} {currency} \n'
