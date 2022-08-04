#! usr/bin/env Python
# coding = utf-8

import nltk
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
             'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1'))

cfd.plot(cumulative=True)

#udhr_text = udhr.raw("Chinese_Mandarin-GB2312")
#nltk.FreqDist(udhr_text).plot(cumulative=True)
