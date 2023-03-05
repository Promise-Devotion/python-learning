import os

import pandas as pd

print(os.getcwd())

filedata = pd.read_csv('./demo/LungCap.csv')
df = pd.DataFrame(filedata)

# 筛选符合条件的数据
male_smokers = df.loc[(df["Gender"] == "female") & (df["Smoke"] == 'yes')]
male_count = df['Gender'].value_counts(ascending=False)

# 统计筛选出的数据的数量
num_male_smokers = male_smokers.shape[0]
print(male_count.male)

print("男性抽烟人数：", num_male_smokers)
