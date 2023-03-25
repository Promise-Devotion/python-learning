import pandas as pd

airports = pd.Series([
    'Seattle-Tacoma', 'Dulles', 'London Heathrow', 'Schiphol', 'Changi',
    'Pearson', 'Narita'
])

print(airports)
print(airports[2])

for value in airports:
    print(value)