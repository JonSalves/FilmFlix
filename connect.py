import sqlite3 as sql

try:

    with sql.connect('filmflix.db') as db_con:
        dbCursor = db_con.cursor()

except sql.OperationalError as oe:
    print(f"Connection Faiel because {oe}")