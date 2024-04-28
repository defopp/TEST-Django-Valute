import json
from requests import request
from datetime import datetime
import sqlite3


# full path to db
# db_path = 'C:\\Users\\pp\\Documents\\code\\stu\\KCSG\\Wallet\\db.sqlite3'

def insert_data_to_sqlite(data:list):
    connect = sqlite3.connect(db_path)
    
    with connect:
        cursor = connect.cursor()
        insert = cursor.executemany('INSERT INTO mainapp_coin(charcode, name, date, rate) VALUES (?,?,?,?)', data)
        connect.commit()
        print('[OK]commited')
        

class CbrParser():

    def get_data():
        return request('get', "https://www.cbr-xml-daily.ru/daily_json.js").text
        
    def data_to_db():
        
        response = CbrParser.get_data()     
        parserd_dict = json.loads(response)

        # DATE with time > DATE
        date = parserd_dict['Date']
        date_to_str = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
        formatted_date = date_to_str.strftime("%Y-%m-%d")
        
        data_to_sql = [(info['CharCode'], info['Name'], formatted_date, info['Value']) for valute, info in parserd_dict['Valute'].items()]
        insert_data_to_sqlite(data_to_sql)
        
    
if __name__ == '__main__':
    CbrParser.data_to_db()
    ...
    
    
    
    
    
    