from pathlib import Path

# Показываем где лежит файл с данымии запоминаем
ROOT_PATH = Path(__file__).parent
PATH_WITH_FIXTURES = Path.joinpath(ROOT_PATH, 'app', 'fixtures', 'operations.json')
