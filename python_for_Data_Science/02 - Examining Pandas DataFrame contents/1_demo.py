import pandas as pd

airports = pd.DataFrame(
    [['Seatte-Tacoma', 'Seattle', 'USA'], ['Dulles', 'Washington', 'USA'],
     ['Heathrow', 'London', 'United Kingdom'],
     ['Schiphol', 'Amsterdam', 'Netherlands'],
     ['Changi', 'Singapore', 'Singapore'], ['Pearson', 'Toronto', 'Canada'],
     ['Narita', 'Tokyo', 'Japan']],
    columns=['Name', 'City', 'Country'])

# print(airports)
"""
Returning first n rows
If you have thousands of rows, you might just want to look at the first few rows

head(n) returns the top n rows
"""
# headline = airports.head(3)
# print(headline)
"""
Returning last n rows
Looking at the last rows in a DataFrame can be a good way to check that all your data loaded correctly

tail(n) returns the last n rows
"""
headline = airports.tail(3)
print(headline)
"""
Checkign number of rows and columns in DataFrame
Sometimes you just need to know how much data you have in the DataFrame

shape returns the number of rows and columns
"""
print(airports.shape)
"""
Getting mroe detailed information about DataFrame contents
info() returns more detailed information about the DataFrame
Information returned includes:

The number of rows, and the range of index values
The number of columns
For each column: column name, number of non-null values, the datatype
"""
print(airports.info())