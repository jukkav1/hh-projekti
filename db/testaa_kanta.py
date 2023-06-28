import sqlite3
import dbfunc

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

dbfunc.hae_merkinta(1, 2)

def oksenna_merkinnat(entries):
    for entry in entries:
        print(f"entry:{entry}")

oksenna_merkinnat()

def tee_merkinta():
    


#inputti sille päivämäärän hakemiselle

