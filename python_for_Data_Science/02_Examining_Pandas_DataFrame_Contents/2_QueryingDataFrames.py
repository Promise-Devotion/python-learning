import pandas as pd

airports = pd.DataFrame(
    [['Seatte-Tacoma', 'Seattle', 'USA'], ['Dulles', 'Washington', 'USA'],
     ['London Heathrow', 'London', 'United Kingdom'],
     ['Schiphol', 'Amsterdam', 'Netherlands'],
     ['Changi', 'Singapore', 'Singapore'], ['Pearson', 'Toronto', 'Canada'],
     ['Narita', 'Tokyo', 'Japan']],
    columns=['Name', 'City', 'Country'])

print(airports)
"""
Return one column
Specify the name of the column you want to return

DataFrameName['columnName']
"""
print(airports['City'])
"""
Return multiple columns
Provide a list of the columns you want to return

DataFrameName[['FirstColumnName','SecondColumnName',...]]
"""
print(airports[['City', 'Country']])
"""
Using iloc to specify rows and columns to return
iloc[rows,columns] allows you to access a group of rows or columns by row and column index positions.

You specify the specific row and column you want returned

First row is row 0
First column is column 0
"""
# print(airports.iloc[0, 0])
print(airports.iloc[2, 2])
"""
A value of : returns all rows or all columns

airports.iloc[:,:]
"""
print("~~~~~~~~~~~~~")
print(airports.iloc[0:2, :])
# Return all rows and display the first two columns
print(airports.iloc[:, 0:2])
"""
You can request a list of rows or a list of columns

[x,y,z] will return rows or columns x,y, and z
airports.iloc[:,[0,2]]
"""

print(airports.iloc[:, [0, 2]])
"""
Using loc to specify columns by name
If you want to list the column names instead of the column positions use loc instead of iloc

airports.loc[:,['Name', 'Country']]
"""
print(airports.loc[:, ['Name', 'Country']])
