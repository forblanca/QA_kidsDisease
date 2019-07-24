from sys import path
path.append('..')
from QA import get_answer
from sentence_pro import stoplist

def main():

    string = input("请输入你的问题：")
    st = stoplist(string)
    ans = get_answer(st)
    print(ans)

if __name__ =="__main__":
    main()