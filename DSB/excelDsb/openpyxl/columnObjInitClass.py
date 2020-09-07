# -*- coding:utf-8 -*-

import openpyxl
class Case:  # 这个类用来存储用例的
    def __init__(self, attrs):
        """
        初始化用例
        :param attrs:zip类型——>[{key,value},(key1,value1)......]
        """
        for i in attrs:
            setattr(self, i[0], i[1])
class ReadExcel(object):
    def __init__(self, filename, sheetname):
        """
        定义需要打开的文件及表名
        :param filename:   文件名
        :param sheetname:  表名
        """
        self.wb = openpyxl.load_workbook(filename)
        self.sheet = self.wb[sheetname]
    def read_data_obj_new(self, list2):
        # 获取最大行数
        max_r1 = self.sheet.max_row
        cases = []
        # 用来存放表头数据
        titles = []
        for row in range(1, max_r1 + 1):
            if row != 1:
                case_data = []
                for column in list2:
                    info = self.sheet.cell(row, column).value
                    # print(info)
                    case_data.append(info)
                case = list(zip(titles, case_data))
                # 新建对象时，将对象传给Case类
                case_obj = Case(case)
                # print(case_obj.caseid,case_obj.excepted,case_obj.data)
                cases.append(case_obj)
            else:
                # 获取表头
                for column in list2:
                    title = self.sheet.cell(row, column).value
                    titles.append(title)
                if None in titles:
                    raise ValueError("传入的表头的数据有显示为空")
        return cases
if __name__ == '__main__':
    r = ReadExcel('cases.xlsx', 'Sheet')
    res1 = r.read_data_obj_new([1, 2, 3])
    print(res1[0].__dir__())
    for i in res1:
        print(getattr(i, '详情页链接'), getattr(i, '商品名称'), getattr(i, '图片链接'))