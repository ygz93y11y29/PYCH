# -*- coding:utf-8 -*-

import openpyxl
class Case:
    pass
class ReadExcel(object):
    def __init__(self,filename,sheetname):
        self.wb = openpyxl.load_workbook(filename)
        self.sh = self.wb[sheetname]
    def read_data_obj(self):
        """
        按行读取数据  每条用例存储在一个对象中
        :return:
        """
        rows_data = list(self.sh.rows)
        # print(rows_data)
        # 获取表单的表头信息
        titles = []
        for title in rows_data[0]:
            titles.append(title.value)
        # print(titles)
        # 定义一个空列表用来存储测试用例
        cases = []
        for case in rows_data[1:]:
            # print(case)
            #创建一个Case类的对象，用来保存用例数据
            case_obj = Case()
            data = []
            for cell in case:  # 获取一条测试用例数据
                # print(cell.value)
                data.append(cell.value)
                # print(data)
            # 将该条数据存放至cases中
            # print(dict(list(zip(titles,data))))
            case_data = list(zip(titles, data))
            # print(case_data)
            for i in case_data:
                #给类添加一个属性和值
                setattr(case_obj,i[0],i[1])
            # print(case_obj)
            # print(case_obj.case_id,case_obj.data,case_obj.excepted)
            cases.append(case_obj)
        return cases
if  __name__ == '__main__':
    r = ReadExcel('cases.xlsx','Sheet')
    res = r.read_data_obj()
    print(res[0].__dir__()[:4])
    for i in res:
        print(getattr(i, '详情页链接'), getattr(i, '商品名称'), getattr(i, '图片链接'),getattr(i, '原价'))