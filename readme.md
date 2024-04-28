##### create venv    
    py -m venv .\venv
##### activate venv
    .\venv\Scripts\activate
##### install req
    pip install -r requirements.txt
##### run server
    cd .\Wallet\
    py manage.py runserver

-----------------------------------
parserapp/valuteparser.py - Добавить полный путь до БД

-----------------------------------


##### Cron строка
    0 0 * * * python (полный путь до)\KCSG\parserapp\valute_parser.py