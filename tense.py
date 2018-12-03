# coding=UTF-8
import re
import jieba
import string

def get_tense(sentence):
    key_words_now = ['最新','這次','今年','現在','用了','用过后','收到后']
    key_words_past = ['早就','老','老的','之前','去年','以前','担心','没有像','听人说','听说','买之前']

    now = sum([key in sentence for key in key_words_now])
    past = sum([key in sentence for key in key_words_past])
    
    if now:
        return 1
    elif past:
        return -1
    else:
        return 0
        


def get_tenses(sentences):   
    tense_list = [get_tense(sentence) for sentence in sentences]
    pre_tense = 0
    for i in range(len(tense_list)):
        if tense_list[i] == 0:          
            tense_list[i] = pre_tense
            pre_tense = 0
        else:
            pre_tense = tense_list[i]
    return tense_list

def split_sentences(text):
    return re.split(r'[^\u4e00-\u9fa5]',text)

def main():
    test = '早就打算买扫地机器人了，只是担心扫不干净，犹豫着！但一直关注着科沃斯这款产品。今年双十一趁着活动，果断买了'
    tense_list = get_tenses(split_sentences(test))
    print (tense_list)
if __name__ == '__main__':
    main()
    