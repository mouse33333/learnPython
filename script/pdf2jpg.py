#! usr/bin/env Python
# coding=utf-8

import fitz

pdf = fitz.open('/Users/Arthur/Downloads/国际中文教育中文水平等级标准-2021.pdf')

for pg in range(0, pdf.pageCount):
    page = pdf[pg]
    trans = fitz.Matrix(5, 5).prerotate(0)
    pm = page.get_pixmap(matrix=trans, alpha=False)
    pm.save('/Users/Arthur/Downloads/HSK_v3/'+str(pg)+".png")
pdf.close()
