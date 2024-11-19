import os

class ExcelFile:
    def __init__(self, file):
        self.file_name = file

    def is_valid_excel(self):
        return os.path.isfile(self.file_name) and ((self.file_name.endswith('.xlsx') or self.file_name.endswith('.xls')))

file_input = input("Enter file name: ")
excel_file_instance = ExcelFile(file_input)
if excel_file_instance.is_valid_excel():
    print("Success")
    # Logic

else:
    print("File does not exist in current directory.\nTry moving the excel file to the current directory.")