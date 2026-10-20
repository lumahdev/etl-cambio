from starter_scripts.db_starter import connection
from db_functions import return_execute_query

result = return_execute_query(connection, """
    SELECT currency_id, iso_code
    FROM currencies;
""")

currency_ids = {
    iso_code: currency_id
    for currency_id, iso_code in result.fetchall()
}

result.close()