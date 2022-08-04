#! usr/bin/env Python
# coding=utf-8

from aip import AipOcr
import time
import xlwt

start_time = time.time()

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("sheet1")

app_id = "16189359"
api_key = "FmgC0K6gkUXOGLPThXsOCOXp"
api_secret = "9IHLc1R8O6sbBLiEpZ9BCeVtktCCFL58"
client = AipOcr(app_id, api_key, api_secret)
count = 0
for num in range(119, 175):
    print(num, count)
    img_left = open("/Users/Arthur/Downloads/HSK_v3/crops/"+str(num)+"_left.png", 'rb').read()
    #print(num, type(img_left), type(img_right))
    result_left = client.basicGeneral(img_left)
    for item in result_left["words_result"]:
        worksheet.write(count, 0, item['words'])
        count = count + 1
    img_right = open("/Users/Arthur/Downloads/HSK_v3/crops/"+str(num)+"_right.png", 'rb').read()
    result_right = client.basicGeneral(img_right)
    for item in result_right['words_result']:
        worksheet.write(count, 0, item['words'])
        count = count + 1

workbook.save('/Users/Arthur/Downloads/HSK_v3/excel.xls')
end_time = time.time()
print('耗时:', int(end_time-start_time), '秒')
