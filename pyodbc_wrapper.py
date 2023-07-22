import pyodbc
from typing import Callable, Any


class SQLServer:
    def __init__(self, host: str, database: str, user: str, 
                 password: str, driver: str = 'ODBC Driver 17 for SQL Server', 
                 port: int = 1433):
        self.connection_string = f'''
                                 Driver={{{driver}}};
                                 Server={host},{port};
                                 DATABASE={database};
                                 UID={user};
                                 PWD={password};
                                 '''
   
    def connect(self):
        self.connection = pyodbc.connect(self.connection_string)
    
    def query(self, query: str, batch_size: int = 10, max_length: int = 2000, 
              cell_transform: Callable[..., Any] = lambda x: x):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            headers = [column[0] for column in cursor.description]
            data = []
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                if max_length and len(data) > max_length:
                    break
                for row in rows:
                    row_dict = dict()
                    for cell, col in zip(row, headers):
                        row_dict[col] = cell_transform(cell)
                    data.append(row_dict)
            return data

    def __delete__(self):
        self.connection.close()
        super().__delete__()
    
