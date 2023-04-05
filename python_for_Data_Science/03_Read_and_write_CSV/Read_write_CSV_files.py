# 读取csv文件
import pandas as pd

# airports_df = pd.read_csv('airports.csv')
# print(airports_df)

# Specify error_bad_lines=False to skip any rows with errors
# airports_df = pd.read_csv('airportsInvalidRows.csv', error_bad_lines=False)
# print(airports_df)
# airports_df = pd.read_csv('airportsNoHeaderRows.csv',
#                           header=None,
#                           names=['Name', 'City', 'Country'])
airports_df = pd.read_csv('airportsBlankValues.csv')
print(airports_df)
airports_df.to_csv('MyNewCSVFile.csv', index=False)