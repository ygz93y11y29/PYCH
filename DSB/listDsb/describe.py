# -*- coding: utf-8 -*-
import time
import tree

##############################################################################
#                                list                                        #
##############################################################################
a = [1, 2, 3, 4, 5, 6, 7]

for el in a:
    if el == 0:
        break
else:
    print('did not break out of for loop ')




#-----------------------------------------------------------------------------filter()  过滤
'''
filter()函数接受2个参数：1个函数对象以及1个可迭代的对象
'''
original_list = [1, 2, 3, 4, 5, 6, 7]
print("filter前:  ", original_list)
def filter_three(number):
    return number>3
filtered = filter(filter_three, original_list)
original_list = list(filtered)
print("filter后:  ", original_list)

#-----------------------------------------------------------------------------列表推导式     过滤
original_list = [1, 2, 3, 4, 5, 6, 7]
print("列表推导式过滤后:    ", [number for number in original_list if number >3])

#----------------------------------------------------------------------------- map()    修改列表
'''
   map()函数使得我们可以将某个函数应用到可迭代对象内每一个元素之上。
'''
original_list = [1, 2, 3, 4, 5, 6, 7]
def square(number):
    return number**2

squares = map(square, original_list)
original_list = list(squares)
print("map后:  ", original_list)

#----------------------------------------------------------------------------- 列表推导式    修改列表
original_list = [1, 2, 3, 4, 5, 6, 7]
print("列表推导式:   ", [number**2 for number in original_list])

#----------------------------------------------------------------------------- zip()        组合列表
'''
    zip()函数接收多个列表作为参数传入，进而得到每个位置上一一对应的元素组合
'''
original_list = [1, 2, 3, 4, 5]
letter = ['a','b','c','d','e']

combind = zip(original_list, letter)
print('zip: ', list(combind))

#-----------------------------------------------------------------------------  颠倒列表
original_list = [1, 2, 3, 4, 5]
print("颠倒列表:    ", original_list[::-1])

#-----------------------------------------------------------------------------max()  次数最多
original_list = [1, 2, 3, 4, 5, 5, 4, 3,4]
set1 = set(original_list)
print('max():   ', max(set1, key=original_list.count))

#-----------------------------------------------------------------------------flatten() 展平嵌套列表
original_list = [[1,2], [[3,4,5],[5,7,8]]]
print("flatten: ", tree.flatten(original_list))


