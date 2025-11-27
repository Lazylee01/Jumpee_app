App Programleírás

    Készítette:
    Szabó Norbert 
    E9SVZ0

Alapadatok

    Program neve: app
    Indítási fájl: main.py
    Alapablak neve: root

Program feladata

    A program egy 2D ügyességi játék, amelyben a játékos célja minél magasabb pontszám elérése úgy,
    hogy egy zöld kör alakú karakterrel deszkákon ugrál felfelé.

    A játék működése:
    
    A játék elején egy START gomb jelenik meg, amelyre kattintva a játék elindul.
    A START gomb alatt rövid vezérlési instrukciók jelennek meg (pl. balra/jobbra irányítás).
    A karakter automatikusan ugrál, a játékos pedig a balra, jobbra nyilakkal irányíthatja.
    Ha a játékos kimegy az ablak bal/jobb szélen, a karakter a másik oldalról bukkan elő.
    A képernyőn megjelenik az aktuális pontszám és a legmagasabb pontszám is.
    Ha a játékos leesik a képernyőről, a játék véget ér, és újrakezdhető a SPACE gombbal.

Oszátlyok, modulok és a modulokban használt függvények

    Saját modul: back_SZN
        Jatekos_SZN()    -      a játékos karakter működéséért felelős osztály
            setIrany()   -      beállítja, hogy a játékos jobbra/balra mozogjon
            rajzol()     -      kirajzolja a karaktert a képernyőre
            mozgas()     -      karakter mozgás logikája
            utkozes()    -      visszaadja a karakter alsó érintkezési pontját
        Deszka()         -      a deszkákért felelős osztály
            mozgas()     -      a deszkák lefelé mozgatása
            rajzol()     -      deszka rajzolása

    Bemutatando modul: pygame
        display.set_mode()    -       alapablak létrehozása
        display.set_caption() -       ablak elnevezése
        font.SysFont()        -       betűtípus létrehozása
        event.get()           -       események lekérése
        quit()                -       program bezárása
        mouse.get_pos()       -       az egér pozíciójának lekérése
        display.update()      -       ablak frissítése
        draw.circle()         -       kör rajzolása
        draw.rect()           -       téglalap rajzolása
        KEYDOWN, KEYUP        –       billentyűesemények
        MOUSEBUTTONDOWN       –       egérkattintás

    Tanult modul: random
        choice()        -     véletlenszerű választás listából  
        randrange()     -     véletlen egész érték generálása a megadott tartományban
        randint()       -     véletlen egész szám generálása  

    Metódusok, függvények
        DeszkaGeneralas()    -   véletlenszerű platformokat generál a pályára
        highscoreLoad()      -   a legmagasabb pontszám fájlbeolvasása
        highscoreSave()      -   a legmagasabb pontszám mentése fájlba
        scoreHozzaadas_SZN() -   a játék során szerzett pontok növelése

    Saját modul:    back_SZN
    Saját osztály:  Jatekos_SZN()
    Saját függvény: scoreHozzaadas_SZN()

Indításhoz szükséges modulok

    pygame  - telepítése: pip install pygame

        
        
    
    
