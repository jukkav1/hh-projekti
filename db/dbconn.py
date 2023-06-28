# tilaa varattu tietokantayhteydelle

import sqlite3
from sqlite3 import Error

file = "kanta.db"

try:
    conn = sqlite3.connect(file)
    print("Hurraa!")
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
