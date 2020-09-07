# -*- coding:utf-8 -*-
from docx2pdf import convert

#*****************************************************************
#                                                                #
#                          文件转pdf格式                          #
#                                                                #
#*****************************************************************
fileName = r'E:\PYCH\DSB\pdfDsb\files'

#-----------------------------------------------------------------------Word转PDF
# convert(r"E:\PYCH\DSB\pdfDsb\files\input.docx", r"E:\PYCH\DSB\pdfDsb\files\output.pdf")
#
# import os
# import glob
# from pathlib import Path
#
# path = os.getcwd() + "\\files\words\\"
# print(path)
# p = Path(path) #初始化构造Path对象
# FileList=list(p.glob("**/*.docx"))
# for file in FileList:
#     convert(file, f"{file}.pdf")


#-----------------------------------------------------------------------Excel转PDF
# import pandas as pd
# import numpy as np
# df_1 = pd.DataFrame(np.random.randn(10, 2), columns=list('AB'))
#
# from fpdf import FPDF
# pdf = FPDF()
# pdf.add_page()
# pdf.set_xy(0, 0)
# pdf.set_font('arial', 'B', 14)
# pdf.cell(60)
# pdf.cell(70, 10, 'Excel to PDF', 0, 2, 'C')
# pdf.cell(-40)
# pdf.cell(50, 10, 'Index Column', 1, 0, 'C')
# pdf.cell(40, 10, 'A', 1, 0, 'C')
# pdf.cell(40, 10, 'B', 1, 2, 'C')
# pdf.cell(-90)
# pdf.set_font('arial', '', 12)
# for i in range(0, len(df_1)):
#     col_ind = str(i)
#     col_a = str(df_1.A.iloc[i])
#     col_b = str(df_1.B.iloc[i])
#     pdf.cell(50, 10, '%s' % (col_ind), 1, 0, 'C')
#     pdf.cell(40, 10, '%s' % (col_a), 0, 0, 'C')
#     pdf.cell(40, 10, '%s' % (col_b), 0, 2, 'C')
#     pdf.cell(-90)
# pdf.output(fileName+'\excels\Excel2PDF.pdf', 'F')

#-----------------------------------------------------------------------PPT转PDF(只能针对Windows)
# import os
# import comtypes
# from comtypes.client import CreateObject
#
#
# #设置路径
# input_file_path = r'E:\PYCH\DSB\pdfDsb\files\ppts\text.ppt'
# output_file_path = r'E:\PYCH\DSB\pdfDsb\files\ppts\text.pdf'
#
# #创建PDF
# powerpoint = CreateObject("Powerpoint.Application")
# powerpoint.Visible = 1
# slides = powerpoint.Presentations.Open(input_file_path)
# #保存PDF
# slides.SaveAs(output_file_path, 32)
# slides.Close()

#-----------------------------------------------------------------------md转pdf
# from markdown2pdf3 import *
# convert_markdown_to_pdf(r'E:\PYCH\DSB\pdfDsb\files\mds\test.md') #你的markdown文件路径

#-----------------------------------------------------------------------html转pdf


