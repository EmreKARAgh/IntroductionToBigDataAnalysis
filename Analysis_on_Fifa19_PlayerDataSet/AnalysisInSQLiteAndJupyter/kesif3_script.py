# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
class sqlite:
    def __init__(self, dbName='buyuk_veri_kesif_3'):
        self.dbPath = dbName+'.db'
        try:
            connection = sqlite3.connect(self.dbPath)
            print('Successfully Connected to Database')
            connection.close()
        except Exception as err:
            print('err:', err)
    def importCSV(self,file='data.csv',table_name='players'):
        df = pd.read_csv(file)
        connection = sqlite3.connect(self.dbPath)
        df.to_sql(table_name, connection, if_exists='replace', index=False)
        connection.close()
    def query(self,sql, database='players'):
        connection = sqlite3.connect(self.dbPath)
        cursor = connection.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
        connection.close()
        return result

#obj = sqlite()
#obj.importCSV('data.csv')
#a = obj.query('select * from players where Name=\'L. Messi\'')
