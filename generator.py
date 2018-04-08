#get text and split into tokens and parts of speech
import nltk
from nltk import pos_tag, word_tokenize

def POS_tagger(list):
    taggedwordlist = nltk.pos_tag(list)

    for word, pos in nltk.pos_tag(list):
        taggedwordlist = nltk.pos_tag(list)

    taglist = [pos for word,pos in taggedwordlist]
    POS_tags = []

    for tag in taglist:
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

        POS_tags.append(POS_tag)
    return POS_tags;

transcript = open('ounupo.txt', 'r')

words = nltk.word_tokenize(transcript.read())
tagged = POS_tagger(words)
