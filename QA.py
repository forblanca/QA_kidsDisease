from numpy.core.defchararray import array

from sentence_pro import keyword,stoplist,fenci
from gensim import models
from numpy import *
import numpy as np

def key_match(sentence):
    """
    关键词进行问题匹配
    :param sentence:
    :return: set是问题的行号
    """
    set = keyword(sentence)
    # print(set)
    set1 = []
    set2 = []
    file = 'q_textrank.txt'
    f = open(file, 'r', encoding='utf8')
    f = f.readlines()
    for s in f:
        list = []
        for word in s.strip().split():
            list.append(word)
        set1.append(list)
    for i in range(len(set1)):
        for j in set:
            if j in set1[i]:
                set2.append(set1[i][0])
                #print("1: ",set2)
    # print("匹配到的标签 - ->",set2)

    num_set = []
    for i in range(len(set2)):
        if i == len(set2):
            break
        else:
            if set2[i] == set2[i-1]:
                num_set.append(set2[i])
    # print(num_set)

    return num_set

def sen_extraction(sentence):

    set2 = []  #问题的候选集合的号码
    set = key_match(sentence)
    s_stop = stoplist(sentence)
    file1 = 'q_pro.txt'
    sentences = open(file1, 'r',encoding='utf8')
    n=0
    for s in sentences:
        if str(n) in set:
            set2.append(s)
        n +=1
    return set2, s_stop

def input_vec(sentence):
    flag = 0
    model2 = models.word2vec.Word2Vec.load('xunlian.model')
    vec = [0 * 64]
    sentence = fenci(sentence)
    for word in sentence:
        flag += 1
        if word == " ":
            continue
        vec += model2[word]
        vec = vec/flag

    return vec


def compute_vec(sentence):
    vec = input_vec(sentence)
    num_set = key_match(sentence)
    f = open("vector.txt", 'r', encoding='utf8')
    f = f.readlines()
    # print(f)

    set = []
    n = 0
    for sentences in f:

        if str(n) in num_set:
            tmp = []
            for i in sentences.strip("[").strip(" [").strip("]\n").split(','):
                if i == '[' or i == ']':
                    continue
                else:
                    tmp.append(float(i))

            A = array(tmp)  # 定义一个数组
            B = array(vec)
            num = float(np.dot(A, B.T))  # 若为行向量则 A * B.T
            denom = linalg.norm(A) * linalg.norm(B)
            cos = num / denom  # 余弦值
            #print(cos)
            sim = 0.5 + 0.5 * cos  # 归一化
            set.append(sim)
        n += 1
    # print(set)

    max = 0
    # a = []
    for i in range(len(set)):
        if max < set[i]:
            max = set[i]
            n = i
    # print(n)
    # print(max)
    # a.append(num_set[n])
    a = num_set[n]

    return int(a)

def get_answer(sentence):

    n = compute_vec(sentence)
    file = open("answer.txt",'r',encoding='utf8')
    f = file.readlines()
    ans = ''
    for i, sen in enumerate(f):
        if i == n:
            ans = sen
            break
    return ans




