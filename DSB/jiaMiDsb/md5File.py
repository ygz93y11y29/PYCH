# -*- coding:utf-8 -*-
import hashlib



'''
    第一种md5key加密方式
'''
str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
print(str_md5)

'''
    第二种md5key加密方式
'''
# 待加密信息
str1 = 'this is a md5 test.'
# 创建md5对象
m = hashlib.md5()
b = str1.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()
print(str_md5)


'''
    列：
'''
# md5加密
s = '123'
m = hashlib.md5(s.encode())
res = m.hexdigest()
print(res)

# MD5加密+加盐
def md5(s, salt=''):
    new_s = str(s) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()

STR = 'fc0caec65b15fdd5a60e8edd768e6d69&1591597239538&12574478&{"q":"鞋架","sst":"1","n":20,"buying":"buyitnow","m":"api4h5","token4h5":"","abtest":"13","wlsort":"13","page":1}'

print(md5(STR))