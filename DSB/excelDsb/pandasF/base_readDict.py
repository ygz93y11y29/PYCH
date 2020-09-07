# -*- coding:utf-8 -*-
import  pandas  as pd
'''
    pandas处理Excel数据成为字典
'''

df=pd.read_excel('cases.xlsx')
test_data=[]
for i in df.index.values:#获取行号的索引，并对其进行遍历：
    #根据i来获取每一行指定的数据 并利用to_dict转成字典
    row_data=df.loc[i,['商品名称','图片链接','原价']].to_dict()
    test_data.append(row_data)
print("最终获取到的数据是：{0}".format(test_data))



