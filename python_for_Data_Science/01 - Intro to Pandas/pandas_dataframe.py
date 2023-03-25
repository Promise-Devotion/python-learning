import pandas as pd

airports = pd.DataFrame(
    [['Seatte-Tacoma', 'Seattle', 'USA'], ['Dulles', 'Washington', 'USA'],
     ['London Heathrow', 'London', 'United Kingdom'],
     ['Schiphol', 'Amsterdam', 'Netherlands'],
     ['Changi', 'Singapore', 'Singapore'], ['Pearson', 'Toronto', 'Canada'],
     ['Narita', 'Tokyo', 'Japan']],
    columns=['Name', 'City', 'Country'])

print(airports)