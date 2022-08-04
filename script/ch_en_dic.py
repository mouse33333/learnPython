#! usr/bin/env Python
# coding=utf-8

import xlwt

# workbook = xlwt.Workbook(encoding="utf-8")
# worksheet = workbook.add_sheet("Sheet1")

word_nature = {"代": "pronoun", "动": "verb", "副": "adverb", "介": "preposition", "连": 'conjunction', "量": 'measure word',
               "名": 'noun', "数": 'numeral', "叹": "interjection", "象": "onomatopoeia", "形": "adjective", "助": "particle"}

word_field = {'[测]': '[surveying and drawing]', '[地理]': '[geography]', '[地质]': '[geology]', '[电]': '[electricity]',
              '[电影]': '[film]', '[电子]': '[electronics]', '[动]': '[zoology]',
              '[法]': '[legal]', '[纺]': '[textile]', '[工美]': '[arts and crafts]',
              '[航海]': '[navigation]', '[航空]': '[aviation]', '[航天]': '[space]',
              '[化]': '[chemistry]', '[化纤]': '[chemical fibre]', '[环保]': '[environmental protection]',
              '[机]': '[mechanics]', '[几何]': '[geometry]', '[计]': '[computer]', '[建]': '[architecture]',
              '[交通]': '[transportation]',
              '[经]': '[economics]', '[军]': '[military]', '[考古]': '[archaeology]', '[矿]': '[mining]',
              '[林]': '[forestry]', '[逻]': '[logic]', '[美]': '[arts]',
              '[牧]': '[animal husbandry]', '[农]': '[agriculture]', '[气]': '[meteorology]', '[商]': '[commerce]',
              '[摄]': '[photography]', '[生]': '[biology]', '[生化]': '[biochemistry]',
              '[生理]': '[physiology]', '[史]': '[history]', '[数]': '[mathematics]',
              '[刷]': '[printing]', '[水]': '[water]', '[体]': '[sports]', '[天]': '[astronomy]', '[铁路]': '[railway]',
              '[统计]': '[statistics]', '[外交]': '[diplomacy]', '[微]': '[bacteriology]', '[无]': '[radio]',
              '[物]': '[physics]', '[戏]': '[theatre]',
              '[心理]': '[psychology]', '[药]': '[pharmacy]', '[冶]': '[metallurgy]', '[医]': '[medicine]',
              '[音]': '[music]',
              '[油]': '[petroleum]', '[渔]': '[fishery]', '[语]': '[linguistics]', '[语音]': '[phonetics]',
              '[杂]': '[acrobatics]',
              '[哲]': '[philosophy]', '[植]': '[botany]', '[中]': '[Chinese medicine]', '[宗]': '[religion]'}

word_expression = {'< 贬>': '[derogatory]', '< 粗>': '[vulgar]', '< 反>': '[antonym]', '< 方>': '[dialect]',
                   '< 古>': '[archaic]', '< 诙>': '[humorous]',
                   '< 讳>': '[offensive]', '< 旧>': '[old]',
                   '< 口>': '[informal]', '< 略>': '[abbreviation]', '< 谦>': '[humble]', '< 书>': '[formal]',
                   '< 套>': '[polite]', '< 婉>': '[euphemistic]',
                   '< 文>': '[literary]', '< 语>': '[grammar]',
                   '< 喻>': '[figurative]', '< 字>': '[literal]', '< 尊>': '[honorific]'}

with open(file=r"/Users/Arthur/PycharmProjects/corpus/cn_en_dict.txt", mode="r", encoding="utf-8") as f:
    ch_en_dict = f.readlines()

with open(file=r"/Users/Arthur/PycharmProjects/corpus/modern_chinese_english_dict2.txt", mode="w", encoding="utf-8") as f2:
    count = 0
    for line in ch_en_dict:
        if line != "\n":
            if len(line) == 2:
                line = line.strip()
                if line in word_nature.keys():
                    line = word_nature[line]+"\n"
                    # print(line)
            for key in word_expression.keys():
                if key in line:
                    line = line.replace(key, word_expression[key])
                    #print(key, '-----', line)
            for key2 in word_field.keys():
                if key2 in line:
                    line = line.replace(key2, word_field[key2])
                    #print(key2, '=====', line)
            f2.write(line)
            count = count + 1
            print(count)

'''
count = 0
for line in dict_list:
    if line == "* * *" and count < (len(dict_list)-1):
        for num in range(1, 100):
            if dict_list[count+num] != "* * *" and count+num < (len(dict_list)-1):
                print(dict_list[count+num])
            else:
                break
    count = count + 1
'''
