import nltk
from nltk import pos_tag, word_tokenize, WhitespaceTokenizer
import sys
from sys import stdin
import random
from termcolor import cprint, colored
''' This part selects the colors that will appear in the terminal '''

color = ["white", "yellow"]
on_color = ["on_red", "on_magenta", "on_blue", "on_grey"]

''' Since nltk has its own way of defining parts of speech,
we replace the codes it uses with parts of speech that we can recognize '''

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

''' Here, we collect all tags defined above into a list, so we can use them later '''
def POS_tagger(words):
    taggedwordlist = nltk.pos_tag(words)

    taglist = [pos for word,pos in taggedwordlist]
    POS_tags = []

    for item in taggedwordlist:
        postag = tags(item[1])
        POS_tags.append([item[0], postag])

    return POS_tags
'''We then check all the words in our text file and we get this function to select random ones,
according to the part of speech in the structure
'''
def givemeone(postag, allthewords):
    filtered = []
    for wordgroup in allthewords:
        if wordgroup[1] == postag:
            filtered.append(wordgroup[0])
    return random.choice(filtered)

''' ...and get all the tags of the words we're using '''
def alltags(allthewords):
    return [t[1] for t in allthewords]

''' By analyzing existing slogans, we selected the most common syntax structures.
You can add your own! '''
structure1 = ['noun', 'not', 'noun']
structure2 = ['verb', 'the', 'noun']
structure3 = ['noun', 'is', 'noun']
structure4 = ['take back the', 'noun']
structure5 = ['gentrification is', 'adjective', 'noun']

''' Now it's time to replace the parts of speech in the structure
with random equivalent words from the text!'''

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
    cprint(' '.join(newlist), random.choice(color), random.choice(on_color))

''' ...and print 10 slogans, just to be sure we get something good. '''
def printmore(structure):
    for _ in range(1, 10):
        doslogan(structure)

''' The program asks you to give your choice of a number here. Then, according to your choice,
it gives you 10 slogans with that exact structure. Enjoy! '''
choice = input('Type a number from 1 to 5: ')
if choice == '1':
    printmore(structure1)
elif choice == '2':
    printmore(structure2)
elif choice == '3':
    printmore(structure3)
elif choice == '4':
    printmore(structure4)
elif choice == '5':
    printmore(structure5)
