# tilaa varattu tietokantafunktioille

# from dbconn import *
import sqlite3
from sqlite3 import Error
from os.path import isfile

kanta = "db/kanta.db"
taulu = "merkinnat2"


def tee_merkinta(paiva, kuukausi, teksti):
    print(f"Koitetaan tehdä merkintä '{teksti}' päivälle {paiva}.{kuukausi}.")
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"INSERT INTO {taulu}(date,month,text) VALUES ('{paiva}', '{kuukausi}', '{teksti}');"
        )
        conn.commit()

    except Error as e:
        print("Joku meni pieleen: ", e)

    finally:
        conn.close()


def hae_merkinta(paiva, kuukausi):
    merkinnat = []
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    if isfile(kanta):
        try:
            x = cursor.execute(f"SELECT * from {taulu} WHERE month IS {kuukausi}")
            for y in x.fetchall():
                merkinnat.append(y)
            return merkinnat
        except Error as e:
            print(e)
            return -1
    else:
        print("kakkaa täh?")

    conn.close()


def test_connection():
    try:
        conn = sqlite3.connect(kanta)
        if conn:
            print("Yhteys toimii.")
    except sqlite3.Error as e:
        print("Ei toimi T_T", e)
    finally:
        conn.close()
