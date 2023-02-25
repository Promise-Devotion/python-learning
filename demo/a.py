import datetime as dt

import pandas as pd

df = pd.DataFrame()

today_date = df['ORDERDATE'].max() + dt.timedelta(days=7)
print(today_date)