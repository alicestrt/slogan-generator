#get text and split into tokens and parts of speech
import nltk
from nltk import pos_tag, word_tokenize, WhitespaceTokenizer
import sys
from sys import stdin
import random

def tags(tag):
    if tag in {"NNP","NNS","NN","NNPS"}:
        POS_tag = 'noun'
    elif tag in {'VB','VBD','VBG','VBN','VBP','VBZ'}:
        POS_tag = 'verb'
    elif tag in {'RB','RBR','RBS','WRB', 'RP'}:
        POS_tag = 'adverb'
    elif tag in {'PRP','PRP$'}:
        POS_tag = 'pronoun'
    elif tag in {'JJ','JJR','JJS'}:
        POS_tag = 'adjective'
    elif tag == 'IN':
        POS_tag = 'preposition'
    elif tag == 'WDT':
        POS_tag = 'determiner'
    elif tag in {'WP','WP$'}:
        POS_tag = 'pronoun'
    elif tag == 'UH':
        POS_tag = 'interjection'
    elif tag == 'POS':
        POS_tag = 'possesive ending'
    elif tag == 'SYM':
        POS_tag = 'symbol'
    elif tag == 'EX':
        POS_tag = 'existential there'
    elif tag == 'DT':
        POS_tag = 'determiner'
    elif tag == 'MD':
        POS_tag = 'modal'
    elif tag == 'LS':
        POS_tag = 'list item marker'
    elif tag == 'FW':
        POS_tag = 'foreign word'
    elif tag == 'CC':
        POS_tag = 'coordinating conjunction '
    elif tag == 'CD':
        POS_tag = 'cardinal number'
    elif tag == 'TO':
        POS_tag = 'to'
    elif tag == '.':
        POS_tag = 'line ending'
    elif tag == ',':
        POS_tag = 'comma'
    else:
        POS_tag = tag
    return POS_tag

def POS_tagger(words):
    taggedwordlist = nltk.pos_tag(words)

    taglist = [pos for word,pos in taggedwordlist]
    POS_tags = []

    for item in taggedwordlist:
        postag = tags(item[1])
        POS_tags.append([item[0], postag])

    return POS_tags

def givemeone(postag, allthewords):
    filtered = []
    for wordgroup in allthewords:
        if wordgroup[1] == postag:
            filtered.append(wordgroup[0])
    return random.choice(filtered)

def alltags(allthewords):
    return [t[1] for t in allthewords]

structure1 = ['noun', 'not', 'noun']
structure2 = ['verb', 'the', 'noun']
structure3 = ['noun', 'is', 'noun']
structure4 = ['take back the', 'noun']
structure5 = ['gentrification is', 'adjective', 'noun']

def doslogan(structure):
    transcript = open('transcription.txt').read()
    words = WhitespaceTokenizer().tokenize(transcript)
    tagged = POS_tagger(words)

    tags = alltags(tagged)

    newlist = []

    for index, item in enumerate(structure):
        if item in tags:
            one = givemeone(item, tagged)
            newlist.append(one)
        else:
            newlist.append(item)
    print('Here are a bunch of slogans you can choose from', ' '.join(newlist))

def printmore(structure):
    for _ in range(1, 10):
        doslogan(structure)


choice = input('Type a number from 1 to 5: ')
if choice == '1':
    printmore(structure1)
elif choice == '2':
    printmore(structure1)

elif choice == '3':
    printmore(structure1)

elif choice == '4':
    printmore(structure1)

elif choice == '5':
    printmore(structure1)
