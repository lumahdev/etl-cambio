import requests
from starter_scripts.db_starter import connection
from currency_dict import currency_ids
from db_functions import execute_many_query

request = requests.get('https://api.frankfurter.dev/v2/rates?base=brl&from=2026-09-01&to=2026-10-17')

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