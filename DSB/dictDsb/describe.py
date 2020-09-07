# -*- coding:utf-8 -*-
###########################################################################
#                          dict                                           *
###########################################################################
from operator import itemgetter

d = {'apple':10, 'orange':30, 'banana':6, 'rotten': 1}
d2 = {'car':55}



print({**d,**d2})

print(dict(d.items()|d2.items()))

d.update(d2)
print(d)

print(sorted(d.items(), key=lambda x:x[1]))

print(sorted(d.items(), key=itemgetter(1)))

print(sorted(d, key=d.get))




















