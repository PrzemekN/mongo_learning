Pycharm proff + python + mongoDB
1. Pobranie/Istalacja/aktualizacja pythona
2. Instalacja pycharma
3. Pobranie/Instalacja mongoDB w wersji community.
    - wybrałem instalację w setup type jako custom, instalacja nie jak service, abu uruchomic server  musze ręcznie go uruchomić z "C:\Program Files\MongoDB\Server\4.4\bin\mongod.exe".
    - bazy beda instalowane w c:\data\db
4. Python potrzebuje drivera do wspólpracy z mongoDB np Pymongo. Zainstalujemy
ten driver za pomoca srodowiska Pycharm w virtualnym srodowisku venv skonfigurowanym wcześniej przy zakładaniu projektu.
    - File -> Settings -> Project <nazwa projektu> -> Python Interpreter,
    po prawej stronie klikamy na ikonę-przycisk + (plus), w oknie Available Packages wpisujemy
    nazwę drivera 'pymongo', ukażę sie nam lista packagów i wybieramy z listy ten o nazwie 'pymongo'
    i na dole ekranu wciskamy Install Package.
5. Aby sprawdzic czy wszystko jest zainstalowane ok, spróbujmy Pycharmie w Python Console wpisać
    'import pymongo', jesli nie pojawia sie błedy tzn że poprawnie zaimportowalismy package.
6. Polaczenie się z serverem i stworzenie nowej bazy danych.
    - aaa
    

LINKI
 - https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
- https://www.w3schools.com/python/python_mongodb_getstarted.asp
