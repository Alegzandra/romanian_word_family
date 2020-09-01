#from nltk.stem.porter import *   # I will use snowball stemmer
import nltk
from nltk.stem import SnowballStemmer
from collections import defaultdict

word_list = []
'''
with open("Lista cuvinte romana a-z.txt", encoding = 'utf-8') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        #print("Line {}: {}".format(cnt, line.strip()))
        word_list.append(line.strip())
        line = fp.readline()
        cnt += 1
fp.close()
'''
with open("Lista cuvinte romana a-z.txt") as fp:
    for line in enumerate(fp):
        word_list.append(line)

print(word_list)


vocab = set(word_list)
print(vocab)
#vocab = set(['grab', 'grabbing', 'grabbed', 'run', 'running', 'eat'])
#vocab = set(['apuca', 'apucând', 'apucat', 'alerga', 'alergând', 'mânca'])

# Here porter stemmer, but can be any other stemmer too
stemmer = SnowballStemmer("romanian")

d = defaultdict(set)
for v in vocab:
    d[stemmer.stem(v)].add(v)  

#print(d)
# defaultdict(<class 'set'>, {'grab': {'grab', 'grabbing', 'grabbed'}, 'eat': {'eat'}, 'run': {'run', 'running'}}
# Now we have a dictionary that maps stems to the valid words that can generate them. For any stem we can do the following:

print(d['apuc'])
# {'grab', 'grabbed', 'grabbing'}

#For building the vocabulary you can tokenize a corpus or use nltk's built-in dictionary of English words.