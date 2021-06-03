from nltk.tokenize import WhitespaceTokenizer
import re
from collections import defaultdict
from collections import Counter
import random

def get_start_words(word_dict):
    start_words = []
    for word in word_dict:
        word1, word2 = word.split()
        if re.match("[A-Z]", word1[0]) and re.match("[^.!?]", word1[-1]):
            start_words.append(word)
    return start_words

filename = input()
file = open(filename, encoding="utf-8")
text = file.read()
file.close()

words = WhitespaceTokenizer().tokenize(text)

word_dict = defaultdict(list)
for i in range(len(words) - 2):
    head = words[i] + " " + words[i + 1]
    tail = words[i + 2]
    word_dict[head].append(tail)

start_words = get_start_words(word_dict)
start_word_list = list(Counter(start_words).keys())
start_freq_list = list(Counter(start_words).values())

for _i in range(10):
    head = random.choices(start_word_list, weights=start_freq_list)[0]
    print(head, end="")
    j  = 2
    while True:
        print(" ", end="")
        tails = Counter(word_dict[head])
        tail = tails.most_common(1)[0][0]
        print(tail, end="")
        j += 1   
        if j >= 5 and re.match("[.!?]", tail[-1]):
            break    
        head1, head2 = head.split()
        head = head2 + " " + tail
    print()
    