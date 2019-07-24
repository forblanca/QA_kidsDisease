from jieba import posseg as pseg
from jieba import analyse
import jieba


def fenci(sentence):
    s = sentence
    # print("开始分词：")
    # print("="*10)
    seg = jieba.cut(s)
    set=[]
    for word in seg:
        set.append(word)
    # print("分词完成")
    return set
def cixing(sentence):
    s = sentence
    # print("开始标注：")
    # print("="*10)
    seg = pseg.cut(s.strip())
    n = 0
    a = 0
    d = 0
    v = 0
    r = 0
    for w, flag in seg:
        if flag == "n":
            n += 1
        elif flag == "a":
            a += 1
        elif flag == "d":
            d += 1
        elif flag == "v":
            v += 1
        elif flag == "r":
            r += 1
    print('分词，词性标注完成')
    return n, a, d, v, r

def length(sentence):
    s = sentence
    l = len(s)
    return l


def stoplist(sentence):
    s = fenci(sentence)
    set=""
    stopwords = [line.strip() for line in open('stoplist.txt', 'r', encoding='utf-8').readlines()]
    for word in s:
        if word not in stopwords:
            set = set + word
            set = set + " "
    return set

def keyword(sentence):
    s = stoplist(sentence)
    tags = analyse.textrank(s, topK=3)
    return tags