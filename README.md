Hyvä Henkäys
===========

Credits
-------
* Arts  &copy; Taru Haapala
* Music &copy; Jani Vähämäki
* Code  &copy; Taru Haapala &amp; Jukka Valvanne
* Database &copy; Jukka Valvanne
* Documentation &copy; Taru Haapala &amp; Jukka Valvanne
* datepicker.kv &copy; el3 &amp; Jukka Valvanne, MIT.

Mitä?
-----
Tehdään hyvinvointisovellus puhelimelle.

# Ohjelma sisältää:
* Vastuunvapautuslause: tämä ei ole virallista terapiaa eikä ohjelmaa ei tule käyttää mielenterveyspaveluiden korvikkeena.
* Konsultoi hoitokontaktiasi ennen ohjelman käyttöä.
* Ääninäytteitä rauhottumista varten.
* pitää kirjaa käyttäjän edistymisestä kalenterilla.

Käyttäjätapauksia
-----------------
- Käyttäjä X haluaa seurata vointiaan ja kirjata havaintoja ylös.
- Käyttäjä Y on todennut rentoutumisharjoitukset hyödylliseksi ja haluaa rentoutua hektisen arjen keskellä, paikasta riippumatta.

# Hyväksymiskriteerit
[x] Ohjelma vastaa käyttäjätarinoiden asettamiin vaatimuksiin.
[x] Ohjelman väriteema on rauhoittava ja saavutettava myös puna-viher / viher-puna / sini-kelta -värisokeille.
[x] Ohjelma pitää kirjaa käyttäjän arviota "voinnista", päiväkirjamerkinnät tallentuvat päivyrin muistiin ja niitä voi lukea.
[x] Toimii android 9+ puhelimella
[/] Koodi on selkeä ja hallittava

Kehittäminen
-------
kehitys käydään kunkin omassa branchissa ja koodimuutokset mergetään Jukan haarassa testattavaksi. Jos muutokset todetaan kehitysympäristössä toimivaksi ja ne katsotaan sopivaksi edistysaskeleeksi, tehdään tästä apk-paketti testattavaksi ja viedään versio dev-x.x.x -haaraan talteen. Näyttötyöversio viedään main-haaraan. jatkokehitys käydään yllä kuvatulla periaatteella.

Asennus
-------
* Koodista ei ole virallisessa levityksessä valmista apk-pakettia; voit rakentaa paketin buildozer-ohjelmalla puhelimellesi.
* Voit windows- tai linux-käyttöjärjestelmällä kuitenkin ajaa ohjelman seuraavasti: 
* 1. kloonata tai ladata tämän haaran koneellesi zip:inä
* 2. asentaa python 3, kivy 2.2 sekä kivymd 1.1-kirjastot vaatimuksineen (pip install -r requirements.txt) koneellesi.
* 3. käynnistä ohjelma python main.py -käskyllä.
