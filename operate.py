import pandas as pd
from tabulate import tabulate
import wcwidth

# 读取
df1 = pd.read_excel('FMRGrp.xlsx')
df2 = pd.read_excel('OMRGrp.xlsx')

# 在合并前重命名df1中的'rate'列，以避免列名冲突
df1_renamed = df1.rename(columns={'rate': '融资比例'})
df2_renamed = df2.rename(columns={'rate': '冲抵比例'})

# 使用merge函数合并两个DataFrame，基于'code'字段
df = pd.merge(df2_renamed, df1_renamed[['code', '融资比例']], on='code', how='left')

# 确保code列是字符串类型
df['code'] = df['code'].astype(str)

# 使用zfill()补充0直到长度为6
df['code'] = df['code'].apply(lambda x: x.zfill(6))

# 使用del语句删除列'B'
del df['date']

# 变更列名
df.rename(columns={'name': '股票名称', 'code': '股票代码', 'stkGroup': '集中度分组'}, inplace=True)

df.to_excel('/Users/lizhuo8/Desktop/StickGrp.xlsx', index=False)

# print(tabulate(df.head(10), tablefmt='fancy_grid'))
