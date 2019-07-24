from gensim import models
import gensim

# 用现成的的语料集
# file2 = "news_12g_baidubaike_20g_novel_90g_embedding_64.bin"
# model = models.KeyedVectors.load_word2vec_format(file2, binary=True)

# 用自己训练队语料集
sentences = []
with open('q_fenci.txt','r',encoding='utf8') as f:
    sentences += [list(line.strip().split()) for line in f]
model = gensim.models.Word2Vec(sentences,
                               size=64,
                               window=5,
                               min_count=1,
                               workers=4)
# print(model["补盐"])
# print('-----------------分割线---------------------------')


#保留模型，方便重用
model.save('xunlian.model')

from gensim import models
import gensim.models.word2vec

model2 = models.word2vec.Word2Vec.load('xunlian.model')
vec = [0*64]
num = 0
out = open('vector.txt', 'w', encoding='utf8')
with open('q_pro.txt','r',encoding='utf8') as f:
    for words in f:
        vec = [0 * 64]
        flag = 0
        if words.isspace():
            out.writelines(" ")
            continue
        else:
            num += 1
            for word in words.strip().split():
                flag += 1
                # print(model2[word])
                vec += model2[word]
            vec = vec/flag
            # print(num)
            # print(type(vec))
            # print(list(vec))
            out.writelines(str(list(vec))+'\n')



f = open("vector.txt", 'r', encoding='utf8')
f = f.readlines()
# print(f)
for sentence in f:
    set = []
    for i in sentence.strip("[").strip("]\n").split(','):
        if i == '[' or i == ']':
            continue
        else:
            set.append(float(i))
    print(set)