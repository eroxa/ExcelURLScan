import pandas as pd
import requests
from requests.exceptions import RequestException

# 👉 Укажи путь к файлу ниже
file_path = ".xlsx"  # Например: "C:/Users/Имя/Downloads/.xlsx"

try:
    # Загрузка таблицы
    df = pd.read_excel(file_path)

    print("Столбцы в файле:", df.columns)

    # Проверим наличие нужного столбца
    if 'Сайт' not in df.columns:
        raise ValueError("В таблице нет столбца с названием 'Сайт'")

    statuses = []

    for url in df['Сайт']:
        print(f"🔍 Проверяю: {url}")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print("✅ Доступен")
                statuses.append("✅ Доступен")
            else:
                print(f"❌ Ошибка {response.status_code}")
                statuses.append(f"❌ Ошибка {response.status_code}")
        except RequestException as e:
            print(f"❌ Недоступен: {e}")
            statuses.append("❌ Недоступен")

    # Добавление столбца со статусами
    df['Статус'] = statuses

    # Сохранение результата
    output_file = "Министерства_РФ_с_проверкой.xlsx"
    df.to_excel(output_file, index=False)

    print(f"\n✅ Проверка завершена. Результат сохранён в: {output_file}")

except FileNotFoundError:
    print(f"❌ Файл не найден по пути: {file_path}")
except Exception as e:
    print(f"❌ Произошла ошибка: {e}")

