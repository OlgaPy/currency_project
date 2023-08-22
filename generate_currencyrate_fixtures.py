import json
import random
from datetime import date, timedelta

# Количество дней для генерации курсов валют
days = 31

# Диапазон случайных курсов валют
min_rate = 1.0
max_rate = 5.0

# Список валют и источников курсов
currencies = [1, 2, 3]
rate_sources = [1, 2]

# Файл для сохранения фикстур
output_file = "currency_app/fixtures/currencyrate_fixtures.json"

# Сгенерировать случайные курсы валют
currency_rates = []
for day in range(days):
    for currency in currencies:
        for rate_source in rate_sources:
            currency_rate = {
                "model": "currency_app.currencyrate",
                "fields": {
                    "date": (date.today() - timedelta(days=days-day-1)).isoformat(),
                    "rate_source": rate_source,
                    "rate": round(random.uniform(min_rate, max_rate), 4),
                    "currency": currency
                }
            }
            currency_rates.append(currency_rate)

# Сохранить фикстуры в файл
with open(output_file, "w") as f:
    json.dump(currency_rates, f, indent=2)

print(f"Фикстуры для CurrencyRate сохранены в файле {output_file}")
