# tilaa varattu tietokantafunktioille
import sqlite3
from sqlite3 import Error
from os.path import isfile

kanta = "db/kanta.db"
taulu = "merkinnat2"


<<<<<<< HEAD
=======
def hae_lista(kk, yy) -> list:
    print("kk", kk, "yy:", yy)

    merkinnat = []
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    if isfile(kanta):
        try:
            x = cursor.execute(f"SELECT * from {taulu} WHERE month IS {kk}")
            for y in x.fetchall():
                merkinnat.append(str(y[0]))
            print("merkinnät kannassa:", merkinnat)
            return merkinnat

        except Error as e:
            print(e)
            return -1
    else:
        print("kakkaa täh?")

    conn.close()


>>>>>>> dev-0.0.7
def tee_merkinta(paiva, kuukausi, vuosi, teksti="Jotain outoa tapahtui!") -> bool:
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


<<<<<<< HEAD
def hae_merkinta(paiva: int, kuukausi: int) -> list:
=======
def hae_merkinta(paiva: int, kuukausi: int, vuosi: int) -> list:
>>>>>>> dev-0.0.7
    merkinnat = []
    conn = sqlite3.connect(kanta)
    cursor = conn.cursor()
    if isfile(kanta):
        try:
            x = cursor.execute(
                f"SELECT * from {taulu} WHERE month IS {kuukausi} and date IS {paiva}"
            )
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
