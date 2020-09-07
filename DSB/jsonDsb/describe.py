# -*- coding:utf-8 -*-
import json
###########################################################################
#                           json                                          *
###########################################################################

''''
    json格式:JSON名称/值对。JSON 数据的书写格式是：名称/值对。名称/值对包括字段名称（在双引号中），然后着是一个冒号(:)，最后是值。
        key只能是string, value可以是 object、array、string、number、true/false、null
        键通过双引号包裹，后面跟冒号“：”，然后跟该键的值；
        值可以是字符串、数字、数组等数据类型；
        对象与对象之间用逗号隔开；
        “{}”用来保存对象；
        “[]”用来保存数组；
'''
'''
    json跟python中的字典看起来很像，两者之间的区别：
        1）json的key只能是字符串，dict的key可以是任何可hash的对象，例如：字符串、数字、元组等；
        2）字典是一种数据结构，json是一种数据格式；字典有很多内置函数，有多种调用方法，而json是数据打包的一种格式，并不像字典具备操作性；
        3）json的字符串强制用双引号，dict的字符串可以用单引号、双引号；
'''
'''
    JSON模块方法：
        json.dumps():将Python中的对象转换为JSON中的字符串对象
        json.dump()：将python对象转换成JSON字符串输出到fp流中。
        json.loads():将JSON中的字符串对象转换为Python中的对象
        json.load():读取包含json对象的文件。
'''

dic = {'name': 'xiaoming', 'age': 29}
json_str = json.dumps(dic)#返回json字符串
print("把字典转换成json串: ", json_str)
print("把字典转换成json串: ", type(json_str))


json_str ='{"id":"09", "name": "Nitin", "department":"Finance"}'
# Convert string to Python dict
dict = json.loads(json_str)
print("把json串转换成字典: ", dict)
print("dict['id']: ", dict['id'])


dic ={
        "name" : "xiaoming",
        "age" : 20,
        "phonenumber" : "15555555555"
    }
with open("test2.json", "w") as outfile:
    json.dump(dic, outfile)


import json
with open('test2.json') as f:
    a = json.load(f)
print("读取文件中的json： ", a, type(a))


