import ast
from collections import Counter
from elmoformanylangs import Embedder
from scipy.spatial import distance
#from sklearn.utils import shuffle
import numpy as np
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity



e = Embedder('C:/Users/Ale/PycharmProjects/lexical_family/env/169/')
sent1 = ['terorist']
sent2 = ['teroare']
#print("ELMO: ", e.sents2elmo(sent), len(e.sents2elmo(sent)[0]))



print(cosine_similarity(e.sents2elmo(sent1), e.sents2elmo(sent2)))

def cosine(a,b):
    a_vals = Counter(a)
    b_vals = Counter(b)

    # convert to word-vectors
    words = list(a_vals.keys() | b_vals.keys())
    a_vect = [a_vals.get(word, 0) for word in words]   #primul cuvant vectorizat
    b_vect = [b_vals.get(word, 0) for word in words]   #al doilea cuvant vectorizat

    # find cosine
    len_a = sum(av * av for av in a_vect) ** 0.5
    len_b = sum(bv * bv for bv in b_vect) ** 0.5
    dot = sum(av * bv for av, bv in zip(a_vect, b_vect))
    cosine = dot / (len_a * len_b)

    return cosine, a_vect, b_vect

print(cosine('terorist','teroare'))

def word_comparison(input_word):
    word_list = []
    with open("lista_cuvinte.txt", encoding='utf-8') as fp:
        for line in enumerate(fp):
            word_list.append(line[1].replace('\n', ''))
    similar_words = []
    for word in word_list:
        if cosine(input_word, word) > 0.95:
            similar_words.append(word)
    return print(similar_words)

#word_comparison('teroare')



