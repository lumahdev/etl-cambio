import requests

from starter_scripts.db_starter import execute_many_query, connection
from currency_dict import currency_ids
from datetime import date, timedelta

yesterday = (date.today() - timedelta(days=1)).isoformat()

request = requests.get(
    "https://api.frankfurter.dev/v2/rates",
    params={"base": "brl", "date": yesterday},
    timeout=30
)

if(request.status_code == 200):
    rates = request.json()

    values = [
        (
            rate["date"],
            currency_ids[rate["quote"].upper()],
            rate["rate"]
        )
        for rate in rates
        if rate["quote"].upper() in currency_ids
    ]

    execute_many_query(connection, """
        INSERT INTO rates (date, quote, rate)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE rate = VALUES(rate);
    """, values)

else:
    print('Não foi possível recuperar os câmbios.')