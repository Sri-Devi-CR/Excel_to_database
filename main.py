import os
import mysql.connector as sql

class Database:    
    def __init__(self, host_inp, user_inp, passwd_inp, file_name):
        self.db = sql.connect(
            host = host_inp,
            user = user_inp,
            passwd = passwd_inp,
            charset = 'utf8',
            database = file_name ### connecting to a db without creating it
        )
        self.cursor = self.db.cursor(buffered=True)
        print("Success")

class ExcelFile:
    def __init__(self, file):
        self.file_name = file

    def is_valid_excel(self):
        return os.path.isfile(self.file_name) and ((self.file_name.endswith('.xlsx') or self.file_name.endswith('.xls')))


file_input = input("Enter excel file name: ")
excel_file_instance = ExcelFile(file_input)
if excel_file_instance.is_valid_excel():
    print("Success")
    
    print("Enter your local database details:\n")
    host = input("Host: ")
    user = input("User: ")
    pwd = input("Database application password: ")

    db_obj = Database(host, user, pwd, file_input)

else:
    print("File does not exist in current directory.\nTry moving the excel file to the current directory.")