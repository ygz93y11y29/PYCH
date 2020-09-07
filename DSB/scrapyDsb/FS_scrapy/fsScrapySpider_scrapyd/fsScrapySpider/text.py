# -*- coding: utf-8 -*-
import time


timeStr = str(time.time())[:14].replace('.', '')

print(timeStr)



print(int(time.time()*1000))