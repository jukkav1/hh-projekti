# tilaa varattu tietokantafunktioille

from dbconn import *


def hae_merkinta(pvm, kuukausi):
    # taru lähti oluelle eikä tee enää töitä

    
    pass


def tee_merkinta():
    pass


import sqlite3

kanta = "kanta.db"


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
