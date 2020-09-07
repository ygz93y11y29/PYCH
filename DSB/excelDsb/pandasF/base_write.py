# -*- coding:utf-8 -*-
import pandas as pd

excelFile = r'cases.xlsx'

sum_list = [[]]
summaryDataFrame = pd.DataFrame(sum_list)
summaryDataFrame.to_excel(excelFile, encoding='utf-8', index=False, header=False)