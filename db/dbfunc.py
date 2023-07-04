# tilaa varattu tietokantafunktioille

# from dbconn import *
import sqlite3
from sqlite3 import Error
from os.path import isfile

kanta = "db/kanta.db"
taulu = "merkinnat"


def tee_merkinta(pvm, kuukausi, teksti):
    # cursor.execute(
    #     f"INSERT INTO merkinnat(date,text) VALUES ('{params[0]}', '{params[1]}');"
    # )

    pass


def hae_merkinnat(pvm, text):
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    params = (pvm, text)
    if isfile(kanta):
        print("Tiedosto on olemassa")
        try:
            x = cursor.execute("SELECT * FROM ?", taulu)
            for y in x.fetchall():
                print(y)

        except Error as e:
            print(e)

    else:
        print("kakkaa täh?")
    conn.close()


def test_connection():
    try:
        conn = sqlite3.connect(kanta)
        if conn:
            print("Yhteys toimii", conn)
    except sqlite3.Error as e:
        print("Ei toimi T_T", e)
    finally:
        conn.close()


test_connection()
