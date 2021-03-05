'''
The program  is  load.py

The program is used to convert given csv files into sqlite database

The code is done in python .The importatnt module used in it is 'csv-to_sqlite'.
They are modules in python ,used to convert csv files into sqlite table direclty

Fisrt need install the csv-to_sqlite using command 'pip install csv-to_sqlite'

After installing we can convert csv files into sqlite tables using method write.csv() of csv-to_sqlite module.
Arguments passed in function is, fisrt one the list of csv files to be converted, second one the name of resultent sqlite table and third the options for converting

refred from https://pypi.org/project/csv2sqlite3/
'''


import csv_to_sqlite 

# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["problem2.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "nba.sqlite", options)