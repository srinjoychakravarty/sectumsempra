from __future__ import division
import glob
import nltk
from string import punctuation

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#Two lists  of words that are used when a man or woman is present, based on Danielle Sucher's Jailbreak the Patriarchy
male_words = set(['guy','spokesman','chairman',"men's",'men','him',"he's",'his','boy','boyfriend','boyfriends','boys','brother','brothers','dad','dads','dude','father','fathers','fiance','gentleman','gentlemen','god','grandfather','grandpa','grandson','groom','he','himself','husband','husbands','king','male','man','mr','nephew','nephews','priest','prince','son','sons','uncle','uncles','waiter','widower','widowers'])
female_words = set(['heroine','spokeswoman','chairwoman',"women's",'actress','women',"she's",'her','aunt','aunts','bride','daughter','daughters','female','fiancee','girl','girlfriend','girlfriends','girls','goddess','granddaughter','grandma','grandmother','herself','ladies','lady','lady','mom','moms','mother','mothers','mrs','ms','niece','nieces','priestess','princess','queens','she','sister','sisters','waitress','widow','widows','wife','wives','woman'])

def gender_the_sentence(sentence_words):
    mw_length = len(male_words.intersection(sentence_words))
    fw_length = len(female_words.intersection(sentence_words))
    if mw_length > 0 and fw_length == 0:
        gender = 'male'
    elif mw_length == 0 and fw_length > 0:
        gender = 'female'
    elif mw_length > 0 and fw_length > 0:
        gender = 'both'
    else:
        gender = 'none'
    return gender

def increment_gender(sentence_words,gender):
    sentence_counter[gender] += 1
    word_counter[gender] += len(sentence_words)
    for word in sentence_words:
        word_freq[gender][word] = word_freq[gender].get(word,0) + 1

def is_it_proper(word):
        if word[0] == word[0].upper():
            case = 'upper'
        else:
            case = 'lower'
        word_lower = word.lower()
        try:
            proper_nouns[word_lower][case] = proper_nouns[word_lower].get(case,0)+1
        except Exception as e:
            #This is triggered when the word hasn't been seen yet
            proper_nouns[word_lower] = {case:1}

sexes = ['male','female','none','both']
sentence_counter = {sex:0 for sex in sexes}
word_counter = {sex:0 for sex in sexes}
word_freq = {sex:{} for sex in sexes}
proper_nouns = {}

file_list = glob.glob('*.txt')

for file_name in file_list:
    # Open the file
    text_bytes = open(file_name,'rb').read()
    # Convert bytes to string
    text = text_bytes.decode('utf-8')
    # Split into sentences
    sentences = tokenizer.tokenize(text)
    for sentence in sentences:
        # word tokenize and strip punctuation
        sentence_words = sentence.split()
        sentence_words = [w.strip(punctuation) for w in sentence_words if len(w.strip(punctuation)) > 0]
        # figure out how often each word is capitalized
        [is_it_proper(word) for word in sentence_words[1:]]
        # lower case it
        sentence_words = set([w.lower() for w in sentence_words])
        # Figure out if there are gendered words in the sentence by computing the length of the intersection of the sets
        gender = gender_the_sentence(sentence_words)
        # Increment some counters
        increment_gender(sentence_words, gender)

# creates a set consisting of all words which were capitalized more often than not
proper_nouns = set([word for word in proper_nouns if
                  proper_nouns[word].get('upper', 0) /
                  (proper_nouns[word].get('upper', 0) +
                  proper_nouns[word].get('lower', 0)) > .50])

# select the top 1,000 words, based on frequencies, from both the male and female word dictionaries
common_words = set([w for w in sorted (word_freq['female'],
                                     key = word_freq['female'].get, reverse = True)[:1000]] + [w for w in sorted (word_freq['male'], key = word_freq['male'].get, reverse = True)[:1000]])

# From the list subtract the words used to identify the sentence as either male or female and subtract with the proper nouns
common_words = list(common_words - male_words - female_words - proper_nouns)

'''
The following computes how likely the word appears in a male subject sentence versus a female subject sentence.
If 'hair' is mentioned in 10 male-subjected sentences and 10 female-subject sentences,
where there is a total of 20 female-subject (50%) sentences and 100 male-subject sentences (10%),
we'll score 'hair' as a 16.6% male, which is (10%)/(50%+10%), and 83.4% female (1:5).
'''

male_percent = {word:(word_freq['male'].get(word,0) / word_counter['male'])
              / (word_freq['female'].get(word,0) / word_counter['female'] + word_freq['male'].get(word,0) / word_counter['male']) for word in common_words}

# print basic statistics on counters about overall rates of coverage
gendered_percentage = (100*(sentence_counter['male'] + sentence_counter['female'])/
                           (sentence_counter['male'] + sentence_counter['female'] + sentence_counter['both'] + sentence_counter['none']))
print(str(gendered_percentage) + " % of sentences in Harry Potter are gendered!")
men_sentences = sentence_counter['male']
print(str(men_sentences) + " sentences in Harry Potter are about men.")
women_sentences = sentence_counter['female']
print(str(women_sentences) + " sentences in Harry Potter are about wommen.")
print("J.K Rowling uses " + str(men_sentences / women_sentences) + " times more sentences about men than about women...")
print("...but that's okay because the main protagonist and antagonist are both male!")

'''
For each of the 50 'most' distinctively male words,
we print the ratio of gendered sentences in which it is used,
along with the count of male-subject and female-subject sentences that had the word.
'''
header = 'Rank\tRatio\tMale\tFemale\tWord'
print('Male words')
print(header)
rank = 1
for word in sorted(male_percent, key = male_percent.get,reverse = True)[:50]:
    try:
        ratio = male_percent[word] / (1 - male_percent[word])
    except:
        ratio = 100
    print('%s\t%.1f\t%02d\t%02d\t%s' % (str(rank), ratio, word_freq['male'].get(word, 0), word_freq['female'].get(word, 0), word))
    rank += 1
'''
For each of the 50 'most' distinctively female words,
we print the ratio of gendered sentences in which it is used,
along with the count of male-subject and female-subject sentences that had the word.
'''
print('\n'*2)
print('Female words')
print(header)
rank = 1
female_words = sorted(male_percent, key = male_percent.get, reverse = False)[:51]
female_words.remove('mione')

for word in female_words:
    try:
        ratio = (1 - male_percent[word]) / male_percent[word]
    except:
        ratio = 100
    print('%s\t%.1f\t%01d\t%01d\t%s' % (str(rank), ratio,word_freq['male'].get(word, 0), word_freq['female'].get(word, 0), word))
    rank += 1
