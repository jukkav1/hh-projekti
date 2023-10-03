# Copyrighted under the MIT license, See LICENSE.
# Copyright (c) 2023 Jukka Valvanne & Taru Haapala

# Tietokantamoduuli
# Otetaan tärkeät kirjastot mukaan
from sqlite3 import connect, Error
from os.path import isfile

# Määritellään kanta ja käytettävä taulu
database = "db/kanta.db"
table = "merkinnat3"


def get_entry_list(month: int, year: int) -> list:
    """Hakee listan kuukauden merkinnöistä ja palauttaa sen listana"""
    entries = []

    # tietokantayhteys
    conn = connect(database)
    cursor = conn.cursor()

    # jos yhteys onnistuu, kysytään koko kuukauden merkinnät kannasta ja laitetaan päivämäärät listaan.
    if isfile(database):
        try:
            query = cursor.execute(
                f"SELECT * FROM {table} WHERE year IS {year} AND month IS {month}"
            )
            for _ in query.fetchall():
                entries.append(str(_[0]))
            return entries

        # joku meni vikaan
        except Error as err:
            print(err)
            return -1

        # suljetaan kanta
        finally:
            conn.close()

    else:
        print("Tiedostoa ei löydy.")


def create_entry(day: int, month: int, year: int, text: str) -> bool:
    """Funktio yrittää tehdä merkinnän päivämäärälle tietokantaan"""
    print(f"tiedot: day: {day}, month: {month}, year: {year}, text: {text}")
    conn = connect(database)
    cursor = conn.cursor()

    # Koitetaan lisätä tauluun päivälle ja kuukaudelle tietty teksti
    try:
        cursor.execute(
            f"INSERT INTO {table} (date,month,year, text) VALUES ('{day}', '{month}', '{year}', '{text}');"
        )
        conn.commit()
        ret_value = True

    # Jos ei onnistu ..
    except Error as err:
        print("Joku meni pieleen: ", err)
        ret_value = err

    # Lopuksi suljetaan kanta ja annetaan paluuarvo
    finally:
        conn.close()
        return ret_value


def get_single_entry(day: int, month: int, year: int) -> list:
    """Hakee yksittäisen merkinnän pop-upia varten"""
    entries = []

    # yhteys kantaan
    conn = connect(database)
    cursor = conn.cursor()

    # jos kanta on, katso mitä sisältää
    if isfile(database):
        try:
            query = cursor.execute(
                f"SELECT * FROM {table} WHERE year IS {year} AND month IS {month} AND date IS {day}"
            )

            # laitetaan listaan ja palautetaan
            for _ in query.fetchall():
                entries.append(_)

        # Joku meni pieleen
        except Error as err:
            print(err)
            entries = -1

        finally:
            conn.close()
            return entries

    # (database) ei ole tiedosto
    else:
        conn.close()
        print("Tiedostoa ei löydy.")
