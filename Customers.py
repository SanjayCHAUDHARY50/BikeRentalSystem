import sqlite3
from BikeRent import BikeRentalCompany
class Customer:
    def __init__(self):
        self.name = None
        self.options = None
        self.bikes = None
        self.total_bill = None
    
    def database(self, name, options, bikes, total_bill):
        try: 
            databaseConnection = sqlite3.connect('database.db')
            curr = databaseConnection.cursor()
            details = [name, options, bikes, total_bill]
            query = '''INSERT INTO CustomerData(name, options, bikes, total_bill)
                    VALUES(?, ?, ?, ?)'''
            curr.execute(query, details)
            databaseConnection.commit()
            databaseConnection.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            databaseConnection.close()
        
    
    def get_details(self):
        try: 
            databaseConnection = sqlite3.connect('database.db')
            curr = databaseConnection.cursor()
            curr.execute('''SELECT * FROM CustomerData''')
            res = curr.fetchall()
            for i in res:
                print(i)
            databaseConnection.commit()
            databaseConnection.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            databaseConnection.close()
    
    def delete_database(self):
        try: 
            databaseConnection = sqlite3.connect('database.db')
            curr = databaseConnection.cursor()
            query = 'DELETE FROM CustomerData'
            curr.execute(query)
            databaseConnection.commit()
            databaseConnection.close()
        except sqlite3.Error as error:
            print("Error in connecting to database : ", error) 
            databaseConnection.close()