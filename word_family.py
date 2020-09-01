import nltk
from nltk.stem import SnowballStemmer
from collections import defaultdict


def generate_words_from_stem(input_word):
    word_list = []
    with open("lista_cuvinte.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            word_list.append(line[1].replace('\n', ''))
    vocab = set(word_list)
    stemmer = SnowballStemmer("romanian")
    d = defaultdict(set)
    for v in vocab:
        d[stemmer.stem(v)].add(v)

    input_word = stemmer.stem(input_word)

    return print(d[input_word])

def generate_words_with_prefixes(input_word):
    word_list = []
    with open("lista_cuvinte.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            word_list.append(line[1].replace('\n', ''))
    prefixes_list = []
    with open("lista_prefixe.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            prefixes_list.append(line[1].replace('\n', ''))
    new_word_list = []
    good_words = []
    for prefix in prefixes_list:
        new_word_list.append(prefix+input_word)
    for word in new_word_list:
        if word in word_list:
            good_words.append(word)
    return print(good_words)

def generate_words_with_sufixes(input_word):
    word_list = []
    with open("lista_cuvinte.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            word_list.append(line[1].replace('\n', ''))
    sufixes_list = []
    with open("lista_sufixe.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            sufixes_list.append(line[1].replace('\n', ''))
    new_word_list = []
    good_words = []
    for sufix in sufixes_list:
        new_word_list.append(input_word+sufix)
    for word in new_word_list:
        if word in word_list:
            good_words.append(word)
    return print(good_words)

def generate_words_with_sufixes_and_prefixes(input_word):
    word_list = []
    with open("lista_cuvinte.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            word_list.append(line[1].replace('\n', ''))
    sufixes_list = []
    with open("lista_sufixe.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            sufixes_list.append(line[1].replace('\n', ''))
    prefixes_list = []
    with open("lista_prefixe.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            prefixes_list.append(line[1].replace('\n', ''))

    new_list = []
    new_list2 = []
    for prefix in prefixes_list:
        new_list.append(prefix+input_word)
    for sufix in sufixes_list:
        for word in new_list:
            new_list2.append(word+sufix)
    #facem verificarea ca exista
    good_words = []
    for word in new_list2:
        if word in word_list:
            good_words.append(word)

    return print(good_words)

#generate_words_from_stem(input("Tastați cuvântul dorit: "))
#generate_words_with_prefixes('calcul')
#generate_words_with_sufixes('calcul')
generate_words_with_sufixes_and_prefixes('teroare')
#generate_words_from_stem('calcul') #nu merge foarte bine
