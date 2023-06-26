# tilaa varattu tietokantafunktioille

# from dbconn import *
import sqlite3
import os.path

kanta = "kanta.db"
taulu = "merkinnat"


def hae_merkinta(pvm, kuukausi):
    pass


def tee_merkinta(pvm, text):
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    params = (pvm, text)
    if os.path.isfile(kanta):
        print("Tiedosto on olemassa")
        #        kanta.execute(f"INSERT into USERS(id, name) VALUES('{id}', '{name}');")

        # cursor.execute(
        #     f"INSERT INTO merkinnat(date,text) VALUES ('{params[0]}', '{params[1]}');"
        # )
        # cursor.execute("SELECT * FROM merkinnat;")
        conn.commit()
        print("Jee")
    else:
        print("kakkaa täh?")
    conn.close()


def test_connection():
    try:
        conn = sqlite3.connect(kanta)
        if conn:
            print("JEE!", conn)
    except sqlite3.Error as e:
        print("fuuu-!", e)
    finally:
        conn.close()
        print("closed")


test_connection()
