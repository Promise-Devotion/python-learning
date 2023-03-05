import os

import matplotlib.pyplot as plt
import pandas as pd

filedata = pd.read_csv('./demo/LungCap.csv')
df = pd.DataFrame(filedata)

# 筛选符合条件的数据
male_smokers = df.loc[(df["Gender"] == "male") & (df["Smoke"] == 'yes')]
male_nosmokers = df.loc[(df["Gender"] == "male") & (df["Smoke"] == 'no')]

female_smokers = df.loc[(df["Gender"] == "female") & (df["Smoke"] == 'yes')]
female_nosmokers = df.loc[(df["Gender"] == "female") & (df["Smoke"] == 'no')]
male_count = df['Gender'].value_counts(ascending=False)

# 统计筛选出的数据的数量
num_male_smokers = male_smokers.shape[0]
num_male_nosmokers = male_nosmokers.shape[0]
num_female_smokers = female_smokers.shape[0]
num_female_nosmokers = female_nosmokers.shape[0]

# print("男性抽烟人数：", num_male_smokers)

male_smoke_percent = num_male_smokers / male_count.male
male_nosmoke_percent = num_male_nosmokers / male_count.male
female_smoker_percent = num_female_smokers / male_count.female
female_nosmoker_percent = num_female_nosmokers / male_count.female

#构建序列
data1 = pd.Series({
    '男性抽烟': male_smoke_percent,
    '男性不抽烟': male_nosmoke_percent,
    '女性抽烟': female_smoker_percent,
    '女性不抽烟': female_nosmoker_percent
})
#将序列的名称设置为空字符，否则绘制的饼图左边会出现None这样的字眼
data1.name = ''
#控制饼图为正圆
plt.axes(aspect='equal')
#防止中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#plot方法对序列进行绘图
data1.plot(
    kind='pie',  #选择图形类型
    colors=["red", "green", "yellow", "blue"],
    autopct='%.2f%%',  #饼图中添加数值标签
    radius=1,  #设置饼图半径
    startangle=180,  #设置饼图的初始角度
    counterclock=False,  #将饼图的顺序设置为顺时针方向
    title='男女抽烟比例',  #为饼图添加标题
    wedgeprops={
        'linewidth': 1.5,
        'edgecolor': 'green'
    },  #设置饼图内外边界的属性值
    textprops={
        'fontsize': 10,
        'color': 'black'
    },  #设置文本标签的属性值
)
#显示图形
plt.show()
