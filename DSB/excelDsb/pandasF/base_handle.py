# -*- coding:utf-8 -*-
import pandas as pd



excelFile = r'cases.xlsx'
df = pd.DataFrame(pd.read_excel(excelFile))
print(df.columns.values)

# 统计 项目
df1 = df[['详情页链接', '商品名称', '图片链接', '原价', '项目', '状态', '数', 'aaa']]
df2 = df1.loc[df1['项目'] == 'KB'].loc[df1['状态'] == 'Completed']

# 获取PM列的值
pmList = df1[['项目']].values.T.tolist()[:][0]
print(pmList)

# 排除重复值
pmList = list(set(pmList))
print(pmList)

for pm in pmList:
    dfByPM = df1.loc[df1['项目'] == pm]
    # print('\r\n')
    #     # print(dfByPM)

sum_list = [['项目', '数']]
for pm in pmList:
    temp = []
    dfByPM = df.loc[df['项目'] == pm]
    for col in dfByPM.columns:
        if col == '数':
            sumValue = dfByPM[col].sum()  # 计数指定列的和
            temp.append(pm)
            temp.append(sumValue)
    sum_list.append(temp)

print(sum_list)



summaryDataFrame = pd.DataFrame(sum_list)
summaryDataFrame.to_excel(excelFile, encoding='utf-8', index=False, header=False)







