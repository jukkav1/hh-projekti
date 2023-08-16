# Tietokantamoduuli

# Otetaan tärkeät kirjastot mukaan
from sqlite3 import connect, Error
from os.path import isfile

# Määritellään kanta ja käytettävä taulu
kanta = "db/kanta.db"
taulu = "merkinnat2"


def hae_lista(kk: int, yy: int) -> list:
    """Hakee listan kuukauden merkinnöistä ja palauttaa sen listana"""
    merkinnat = []

    # tietokantayhteys
    conn = connect(kanta)
    cursor = conn.cursor()

    # jos yhteys onnistuu, kysytään koko kuukauden merkinnät kannasta ja laitetaan päivämäärät listaan.
    if isfile(kanta):
        try:
            x = cursor.execute(f"SELECT * FROM {taulu} WHERE month IS {kk}")
            for _ in x.fetchall():
                merkinnat.append(str(_[0]))
            return merkinnat

        # joku meni vikaan
        except Error as err:
            print(err)
            return -1

        # suljetaan kanta
        finally:
            conn.close()

    else:
        print("Tiedostoa ei löydy.")


def tee_merkinta(paiva: int, kuukausi: int, vuosi: int, teksti: str) -> bool:
    """Funktio yrittää tehdä merkinnän päivämäärälle tietokantaan"""
    conn = connect(kanta)
    cursor = conn.cursor()

    # Koitetaan lisätä tauluun päivälle ja kuukaudelle tietty teksti
    try:
        cursor.execute(
            f"INSERT INTO {taulu}(date,month,text) VALUES ('{paiva}', '{kuukausi}', '{teksti}');"
        )
        conn.commit()
        r = True

    # Jos ei onnistu ..
    except Error as e:
        print("Joku meni pieleen: ", e)
        r = False

    # Lopuksi suljetaan kanta ja annetaan paluuarvo
    finally:
        conn.close()
        return r


def hae_merkinta(paiva: int, kuukausi: int, vuosi: int) -> list:
    """Hakee yksittäisen merkinnän pop-upia varten"""
    merkinnat = []

    # yhteys kantaan
    conn = connect(kanta)
    cursor = conn.cursor()

    # jos kanta on, katso mitä sisältää
    if isfile(kanta):
        try:
            x = cursor.execute(
                f"SELECT * FROM {taulu} WHERE month IS {kuukausi} AND date IS {paiva}"
            )

            # laitetaan listaan ja palautetaan
            for y in x.fetchall():
                merkinnat.append(y)

        # Joku meni pieleen
        except Error as e:
            print(e)
            merkinnat = -1

        finally:
            conn.close()
            return merkinnat

    # (kanta) ei ole tiedosto
    else:
        conn.close()
        print("Tiedostoa ei löydy.")
