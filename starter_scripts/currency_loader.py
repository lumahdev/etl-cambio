import requests
from starter_scripts.db_starter import execute_query, connection

request = requests.get('https://api.frankfurter.dev/v2/currencies')

if(request.status_code == 200):
    currencies = request.json()

    for currency in currencies:

        execute_query(connection, """
            INSERT INTO currencies (iso_code, iso_numeric, name, symbol)
            VALUES (%s, %s, %s, %s);
            """,
            (
                currency["iso_code"],
                currency["iso_numeric"],
                currency["name"],
                currency["symbol"]
            )
        )

else:
    print('Não foi possível recuperar as moedas.')