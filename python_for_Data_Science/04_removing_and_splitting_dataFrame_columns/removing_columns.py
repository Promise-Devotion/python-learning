import pandas as pd

delays_df = pd.read_csv('flight_delays.csv')

# delays_df.head(n) n默认值是5

# 删除某一列drop方法
new_df = delays_df.drop(columns=['AIR_TIME'])
print(new_df.head(10))