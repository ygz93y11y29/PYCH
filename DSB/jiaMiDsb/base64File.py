# -*- coding:utf-8 -*-
import hashlib, base64




# sha256加密
m = hashlib.sha256(s.encode())
res = m.hexdigest()
print(res)

# base64加密
m = base64.b64encode(s.encode())
res = m.decode()
print(res)

# base64解密
b = base64.b64decode('MTIz')
res = b.decode()
print(res)