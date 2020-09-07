# -*- coding:utf-8 -*-

import openpyxl
class Case:
    pass
class ReadExcelZy(object):
    def __init__(self,filename,sheetname):
        self.wb = openpyxl.load_workbook(filename)
        self.sheet = self.wb[sheetname]

        # list1 参数为一个列表，传入的是指定读取数据的列,比如[1,2,3]
        # 每一行[1,3,5]列的数据，读取出来就作为一条测试用例，放在字典中
        # 所有的用例放在对象中并且进行返回
    def read_data_obj(self,list2):
        max_r1 = self.sheet.max_row      #获取最大行数
        cases = []
        titles = []      #用来存放表头数据
        for row in range(1,max_r1+1):
            if row != 1:
                case_data = []
                for column in list2:
                    info = self.sheet.cell(row,column).value
                    # print(info)
                    case_data.append(info)
                cases_data = list(zip(titles,case_data))
                #将一条用例存到一个对象中（每一列对应对象的一个属性）
                case_obj = Case()
                for i in cases_data:
                    # print(i)
                    setattr(case_obj,i[0],i[1])
                # print(case_obj.caseid,case_obj.excepted,case_obj.data)
                cases.append(case_obj)
            else:
                for column in list2:
                    title = self.sheet.cell(row,column).value
                    titles.append(title)
        return cases
if __name__ == '__main__':
    r = ReadExcelZy("cases.xlsx","Sheet")
    res = r.read_data_obj([1,2,3])
    print(res[0].__dir__())
    for i in res:
        print(getattr(i, '详情页链接'), getattr(i, '商品名称'), getattr(i, '图片链接'))