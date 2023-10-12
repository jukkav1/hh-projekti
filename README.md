hh-projekti
===========

Credits
-------
* Arts by Taru Haapala
* Music by Jani Vähämäki
* Code by Taru Haapala and Jukka Valvanne
* Database by Jukka Valvanne
* Documentation by Taru Haapala and Jukka Valvanne

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

Käyttöoikeudet [fin]
--------------
Ohjelmakoodi on lisensoitu MIT:n alle, eli ohjelmakoodia saa käyttää, kopioida, muokata sekä levittää vapaasti haluamallaan tavalla sillä edellytyksellä, että ohjelman ja/tai sen osan tekijät mainitaan nimeltä. Kts. LICENSE.

Ohjelman sisältämät kuvat ja äänipätkät kansioissa `images` sekä `sounds` ovat osa tätä ohjelmaprojektia, eikä niitä saa muuttaa tai käyttää muussa yhteydessä ilman tekijöiden lupaa. Saat kuitenkin korvata ne halutessasi omilla tiedostoilla, mikäli kyseisten tiedostojen käyttöoikeudet niin sallivat.

Licencing [eng]
-------
This software is licensed under MIT, meaning you are free to use, copy, modify and redistribute it by any means, given you attribute the code to its original author. See LICENSE.

The pictures and sounds in `images` and `sounds` folders belong to this specific project, and may NOT be modified or used elsewhere without permission granted by their authors. How ever, you are free to replace them with any other piece of work, given the licence of replacement permits this.