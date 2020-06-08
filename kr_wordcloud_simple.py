import os

from os import path
from konlpy.tag import Hannanum
from wordcloud import WordCloud

"""This code is to generate and to plot a wordcloud in Korean version. 
Of course it is possible to generate a simple wordcloud with the original codes. However
due to the major difference with English and complexity, the result from the original codes will not
be as perfect as we expected.

The major difference between English and Korean(Hangul) is that English words can be devided by space(' ')
while Korean words cannot be divided by space. To make a Korean sentence, every single noun has to be combined with
articles without space(ex. I am --> 나는, 나:I 는:am).

For this reason, even though the text want to say 'I' in every appearance as '나는','나를', '나에게',
the original codes will separate these words as a different meaning and a different word.
'"""

"""To implement the codes, you must install konlpy package which is a module for natural language processing for Korean.

It provides a function with separating the main words and articles, and only extract the main words."""

"""So don't forget to install konlpy package!"""

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


#get the path of Korean_fonts otf file
font_path = d + '/word_cloud/examples/fonts/NotoSansKR/NotoSansKR-Black.otf'

def listToString(list1):
    str=" " #distinguish nouns by 'space'

    return (str.join(list1))

def get_string(path):
    f = open(path, "r", encoding="utf-8")
    sample = f.read()
    f.close()
    h = Hannanum()
    list_nouns = h.nouns(sample) #get list of nouns from sample
    return listToString(list_nouns) #get string of list_nouns

path = d + '/word_cloud/kor_text/2020.05.28.기사1.txt' #path of korean text

tags = get_string(path)  # tags : string of list_nouns
wc = WordCloud(font_path=font_path, background_color="white",
               max_font_size=100, random_state=42, width=1000, height=860, margin=2) #collocations=false

#display the generated image
wordcloud = wc.generate(tags)
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation ='bilinear')
plt.axis("off")
plt.show()
