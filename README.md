Autókatalógus Program 

Készítette: Kleiner Bence
Program neve: Autókatalógus KB

Program célja

Az Autókatalógus egy egyszerűen kezelhető grafikus Python alkalmazás, amely autók adatainak megtekintését, hozzáadását, módosítását, törlését, keresését és TXT fájlba történő mentését teszi lehetővé.
A program induláskor 20 előre betöltött autót tartalmaz.

Indítás

A projekt indítófájlja: main.py
Indítás parancssorból:

python main.py

A main.py létrehozza az alkalmazás alap tkinter ablakát (root), majd betölti az alkalmazást (app).

Program felépítése

A projekt két fő részből áll:

main.py
– létrehozza és elindítja a programot
– inicializálja a grafikus felületet

autokatalogus_KB.py
– tartalmazza a teljes program működését
– tartalmazza az osztályokat, függvényeket, eseménykezelést és a grafikus felületet

A program működése

A grafikus felület egyetlen fülből áll, amely a következő részeket tartalmazza:

Adatbevitel
A felhasználó itt adhatja meg az autó adatait: rendszám, márka, modell, év, szín, ár.
A rendszám kötelező formátuma: három nagybetű, kötőjel, három szám (AAA-111).

Műveleti gombok
– Hozzáadás
– Módosítás
– Törlés
– TXT mentés
– Kilépés

Keresés
A keresőmezőbe írt szöveg alapján a lista valós időben szűrődik márka, modell, rendszám vagy szín szerint.

Lista
A listában minden autó egy sorban jelenik meg.
A kijelölt sor adatai automatikusan bekerülnek az adatmezőkbe.

Státuszsor
A program jelzi a találatok számát és az utolsó végrehajtott műveletet.

Hibakezelés

A program a következő hibákat kezeli:

– Hibás rendszámformátum (AAA-111 helyett más megadás)
– Üres vagy hiányzó adat
– Már létező rendszám hozzáadása
– Érvénytelen szám a „év” vagy „ár” mezőben

Hiba esetén felugró üzenet jelzi a problémát.

TXT mentés

A „TXT mentés” gombbal a lista teljes tartalma elmenthető szövegfájlba.
A fájl minden sora egy autó adatait tartalmazza olvasható formában:

AAA-111 | Toyota Corolla | 2018 | fehér | 4 490 000 Ft

Kilépés

A „Kilépés” gomb bezárja az alkalmazást.
Behívott függvény: self.gyoker.destroy()

Felhasznált modulok

– tkinter (grafikus felület)
– ttk (modern felületi elemek)
– messagebox (hibák és üzenetek)
– filedialog (TXT mentés)
– dataclasses (Auto osztály)
– re (rendszám ellenőrzése)
– math (árkonverzió és kerekítés)

Saját modul, osztály és függvények

A projekt saját modulja: autokatalogus_KB.py
A monogram (KB) minden saját elemben szerepel.

Saját osztály:
– KatalogusKB (autók listakezelése)

Saját függvények:
– szam_egesz_KB()
– szam_penz_KB()
– rendszam_ellenorzes_KB()
– penz_formaz_KB()
– demo_autok_KB()
