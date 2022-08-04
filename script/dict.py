#! usr/bin/env Python
# coding=utf-8

from translate import Translator
import xlrd
import xlwt
import json
import urllib
import random
import hashlib
import os
from pypinyin import pinyin

appid = '20211028000985582'
secretKey = '_KpvXoPEEvHbXEI0jBXU'
url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

number_100 = []
for i in range(100):
    number_100.append(str(i))

word_nature = {"代": "pronoun", "动": "verb", "副": "adverb", "介": "preposition", "连": 'conjunction', "量": 'measure word',
               "名": 'noun', "数": 'numeral', "叹": "interjection", "象": "onomatopoeia", "形": "adjective", "助": "particle"}

# 返回拼音
def pinyin_com(text):
    pinyin_list = pinyin(text)
    text_pinyin = ""
    for num in range(len(pinyin_list)):
        if len(pinyin_list) == 4 and num == 2:
            text_temp = pinyin_list[num][0]
            text_pinyin = text_pinyin + "-" + text_temp
        else:
            text_temp = pinyin_list[num][0]
            text_pinyin = text_pinyin + text_temp
    return text_pinyin

# 百度翻译
def translateBaidu(text, f='zh', t='en'):
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + f + '&to=' + t + \
          '&salt=' + str(salt) + '&sign=' + sign
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    result = str(data['trans_result'][0]['dst']).lower()
    return result


workbook = xlrd.open_workbook("/Users/Arthur/Downloads/HSK_v3/HSK_v3_Level7~9.xls")
worksheet = workbook.sheet_by_index(0)
rows = worksheet.nrows

workbook_out = xlwt.Workbook(encoding="utf-8")
worksheet_out = workbook_out.add_sheet("Sheet1")
translator = Translator(from_lang="chinese", to_lang="english")

with open("/Users/Arthur/PycharmProjects/corpus/modern_chinese_english_dict2.txt", mode="r", encoding="utf-8") as txt:
    dict_list = list(txt.readlines())
    # print(dict_list)

# 返回词典释义
def get_english(text):
    count1 = 0
    explanation = []
    exp = []
    if len(text) == 1:
        text = text + " " + "[" + pinyin_com(text) + "]"
    for line in dict_list:
        line = line.strip()
        if text == line:
            for num in range(1, 1000):
                if dict_list[count1 + num] == "* * *\n":
                    break
                else:
                    explanation.append(dict_list[count1 + num].strip())
        count1 = count1 + 1
    # print("full:", explanation)
    count2 = 0
    for item in explanation:
        index = explanation.index(item)
        if item in word_nature:
            exp.append(item + "\n")
        if item[0:2] in number_100:
            exp.append(item + "\n")
        if item[0:1] != "♦" and item[0:1] != "另":
            exp.append(item + "\n")
        count2 = count2 + 1
    if len(exp) > 0:
        exp[len(exp)-1] = exp[len(exp)-1].strip()
    return exp


#print(get_english("耙"))
#print(get_english("阿门"))

count = 0
for num in range(10):
    count += 1
    cell_value = worksheet.cell_value(num, 0)
    #trans_google = translator.translate(cell_value).lower()
    trans_baidu = translateBaidu(cell_value)
    trans_dict = get_english(cell_value)
    #print(cell_value, ":", trans_dict)
    pinyin_col = pinyin_com(cell_value)
    worksheet_out.write(num, 0, cell_value)
    worksheet_out.write(num, 1, pinyin_col)
    worksheet_out.write(num, 2, trans_baidu)
    #worksheet_out.write(num, 3, trans_google)
    worksheet_out.write(num, 4, trans_dict)
    #print(count, cell_value, ":", pinyin_col, ";")
    #[print(item.strip()) for item in trans_dict]
    #print("\n")

workbook_out.save('/Users/Arthur/Downloads/HSK_v3/out.xls')
os.system("open /Users/Arthur/Downloads/HSK_v3/out.xls")
