try:
    import pymongo
except ImportError:
    print(f"nie mogę zaladowac biblioteki 'pymongo")
    exit()

try:
    import logging
except ImportError:
    print(f"nie mogę zaladowac biblioteki 'logging' ")
    exit()

from pymongo.errors import ConnectionFailure


# ======================================================
# legenda mongoDB: Server   Baza    Kolekcja(odpowiednik tablicy w sql)    Dokument(odpowiednik rekord/wiersz w sql)

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print_hi('PyCharm')

    # utworzenie obiektu klienta MongoClient z podaniem adresu servera
    db_server = "mongodb://localhost:27017/"
    logging.info(f"łacze się z serverem...{db_server}")
    myclient = pymongo.MongoClient(db_server, serverSelectionTimeoutMS=5000)
    try:
        # The ismaster command is cheap and does not require auth.
        myclient.admin.command('ismaster')
    except ConnectionFailure as err:
        logging.error(f"Server jest niedostepny, {err}")
        exit()

    nazwa_bazy = "moja_baza"
    # wyswietlamy nazwy wszystkich baz danych
    dblist = myclient.list_database_names()
    print(f"lista wszystkich nazw baz danych:{dblist}")
    logging.info(f"lista wszystkich nazw baz danych:{dblist}")
    if nazwa_bazy in dblist:
        print("Baza danych istnieje juz na tym serverze wiec nie jest na nowo tworzona/nadpisywana.")
        # poniewaz baza danych istniała wiec ustawiam sie na bazie danych
        mydb = myclient["moja_baza"]  # lub tak: myclient.moja_baza
    else:
        # utworzenie bazy danych
        mydb = myclient["moja_baza"]  # lub tak: myclient.moja_baza
        print(myclient.list_database_names())
        # zauważ ze po ponownym sprawdzeniu nazw bazy, niestety nie ma naszej nowo utworzonej bazy! ?
        # ponieważ w mongodb baza zostanie utworzona jesli bedzie miala kolekcję i choc jeden dokument w kolekcji.

    # wyswielamy liste wszystkich kolekcji w bazie danych
    nazwa_kolekcji = "Przemka kolekcyjum"
    lista_kolekcji = mydb.list_collection_names()
    print(f"lista wszystkich kolekkcji w bazie '{nazwa_bazy}': {lista_kolekcji}")
    if nazwa_kolekcji in lista_kolekcji:
        print(f"kolekcja '{nazwa_kolekcji}' istnieje już w bazie '{nazwa_bazy}'")
        # poniewaz baza danych i kolekcja  istniała wiec ustawiam sie na kolekcji i kolekcja nie jest nadpisywana
        moja_kolekcja = mydb[nazwa_kolekcji]
    else:
        # tworzymy kolekcję (odpowiednik tablicy w sql)
        # Uwaga w mongoDB kolekcja nie zostanie utworzona dopóki nie bedzie zawierała choc jednego
        # dokumentu(rekordu/wiersza)
        moja_kolekcja = mydb[nazwa_kolekcji]

    # dodajemy dokument do kolekcji
    dane1 = {"firstname": "Przemek", "surname": "Nawrocki"}
    x = moja_kolekcja.insert_one(dane1)

    # teraz gdy stworzyłem dokument sprawdzam czy bazadanych i kolekcja zostaly zalozona
    print(myclient.list_database_names())
    print(mydb.list_collection_names())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
