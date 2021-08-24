from __future__ import unicode_literals
from hazm import *
import docx2txt
MY_TEXT = docx2txt.process("paragraphs.docx")
def pre_process(text):
    print('normalized text is:')
    normalizer = Normalizer()
    text = normalizer.normalize(text)
    print(text)
    return text

def numberOfSentences(paragraphs):
    numOfSentences = []
    tokenizer = SentenceTokenizer()
    i=0
    for text in paragraphs:
        sentences = tokenizer.tokenize(text)
        numOfSentences.append(len(sentences))
        i+=1
    return numOfSentences

def extractPartOfSpeech(paragraphs, numOfSentences):
    tagger = POSTagger(model='resources/postagger.model')
    wordTokenizer = WordTokenizer()
    paragraphs_info = []
    counter = 1
    for paragraph in paragraphs:
        verbsCount = 0
        nounsCount = 0
        print('normalized paragraph '+str(counter)+':')
        print(paragraph+'\n')
        paragraphTokens = wordTokenizer.tokenize(paragraph) #array of tokens of paragraph
        taggedTokens = tagger.tag(paragraphTokens)  #array of tagged tokens
        print('tagged tokens of paragraph '+str(counter)+':')
        print(str(taggedTokens)+'\n')
        wordsCount = len(taggedTokens)
        for token in taggedTokens:
            if token[1] == 'V':
                verbsCount += 1
            elif token[1] == 'N':
                nounsCount += 1

        paragraphs_info.append({'paragraphId': str(counter),
                                'numberOfSentences': numOfSentences[counter-1],
                                'wordsCount': wordsCount,
                                'verbsCount': verbsCount,
                                'nounsCount': nounsCount})
        counter += 1

    return paragraphs_info

def fivesentences(paragraphs):
    # print('number of sentences for each paragraph:')
    global sen
    tokenizer = SentenceTokenizer()
    tokenizer1= WordTokenizer()
    stemmer = Stemmer()
    allSentences = []
    for text in paragraphs:
        sentences = tokenizer.tokenize(text) #find sentences in paragraph
        for sen in sentences:
            allSentences.append(sen)

    counter = 1
    for sentence in allSentences:
        if(counter != 6):
            print('sentence '+str(counter)+':')
            print(sentence)
            print('stems of sentence '+str(counter)+':')
            stem_list = []
            x = tokenizer1.tokenize(sentence) #find tokens of one sentence
            for element in x: #for each token of sentence wana find stem
                if "." not in element and "،" not in element and "..." not in element:
                    if not element.isdigit():
                        el = stemmer.stem(element)
                    stem_list.append(el)
            print(str(stem_list)+'\n')
            counter += 1


#part 1
normalized_text = pre_process(MY_TEXT)

#part 2
paragraphs_list = normalized_text.split('\n\n') #seperate paragraphs
numOfSentences = numberOfSentences(paragraphs_list)
paragraphs_info = extractPartOfSpeech(paragraphs_list,numOfSentences)
print('information of all paragraphs:')
print(str(paragraphs_info)+'\n')

#part 3
fivesentences(paragraphs_list)

'''def pre_process(text):
    normalizer = Normalizer()
    text = normalizer.affix_spacing(text) # فاصله میان پیشوند‌ها و پسوند‌ها را اصلاح می‌کند.
    text = normalizer.character_refinement(text) # اصلاح کاف و یای عربی
    text = normalizer.punctuation_spacing(text) # اصلاح (پرانتزها) و فاصله نقطه و ویرگول از کلمه بعد در متن.
    print(text)
'''