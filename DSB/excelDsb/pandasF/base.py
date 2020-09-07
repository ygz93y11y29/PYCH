# -*- coding:utf-8 -*-
import  pandas  as pd
'''
    一：读取Excel文件的两种方式：
            得到的结果是一个二维矩阵
'''
#方法一：默认读取第一个表单
df=pd.read_excel('cases.xlsx')#这个会直接默认读取到这个Excel的第一个表单
data=df.head()#默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data))#格式化输出

#方法二：通过指定表单名的方式来读取
df=pd.read_excel('cases.xlsx',sheet_name='Sheet')#可以通过sheet_name来指定读取的表单
data=df.head()#默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data))#格式化输出

#方法三：通过表单索引来指定要访问的表单，0表示第一个表单
#也可以采用表单名和索引的双重方式来定位表单
#也可以同时定位多个表单，方式都罗列如下所示
df=pd.read_excel('cases.xlsx',sheet_name=['Sheet','Sheet1'])#可以通过表单名同时指定多个
# df=pd.read_excel('cases.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# df=pd.read_excel('cases.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# df=pd.read_excel('cases.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
#sheet_name=None: 获取的是所有的表单

print(df.keys())#获取表单名
data=df.values#获取所有的数据，注意这里不能用head()方法哦~
print("*获取到所有的值:\n{0}".format(data))#格式化输出   结果是：builtin_function_or_method类型


#
# df=pd.read_excel('cases.xlsx',sheet_name=None)
# print(df.keys())
# print(df[list(df.keys())[0]])












