# -*- coding:utf-8 -*-
import  pandas  as pd

'''
    二： pandas操作Excel的行列
    
'''
df=pd.read_excel('cases.xlsx')  #这个会直接默认读取到这个Excel的第一个表单


#1：读取指定的单行，数据会存在列表里面
data=df.loc[0].values
data=df.iloc[0].values     #0表示第一行 这里读取数据并不包含表头，要注意哦！
print("读取指定行的数据：\n{0}".format(data))


#2：读取指定的多行，数据会存在嵌套的列表里面：
data=df.loc[[1,2]].values#读取指定多行的话，就要在ix[]里面嵌套列表指定行数
print("读取指定行的数据：\n{0}".format(data))


#3：读取指定的行列：
data=df.iloc[1,2]#读取第一行第二列的值，这里不需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))


#4：读取指定的多行多列值：
data=df.loc[[1,2],['详情页链接','商品名称']].values#读取第一行第二行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))


#5：获取所有行的指定列
data=df.loc[:,['详情页链接','商品名称']].values#读所有行的title以及data列的值，这里需要嵌套列表
print("读取指定行的数据：\n{0}".format(data))
data1 = df[['详情页链接','商品名称']].values
print("读取指定行的数据：\n{0}".format(data1))

#6：获取行号并打印输出
print("输出行号列表",df.index.values)


#7：获取列名并打印输出
print("输出列标题",df.columns.values)


#8：获取指定n行数的值：
print("输出值",df.sample(3).values)#这个方法类似于head()方法以及df.values方法


#9：获取指定列的值：
print("输出值\n",df['商品名称'].values)

#10: 获取连续行的某列的值：
data = df[1:10]['详情页链接']


#11.获多行多列的值：
data1 = df[["详情页链接",'原价']][2:5]   #等于   df.loc[2:5,["详情页链接",'原价']]


