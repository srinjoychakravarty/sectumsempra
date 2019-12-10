import nltk, os, pickle
from io import StringIO
from nltk import pos_tag, word_tokenize
from os import listdir
from os.path import isfile, join
from pdfminer.converter import TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import resolve1
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from tika import parser
from collections import Counter

def count_pages(path):
    '''
    Count the number of pages in the book
    '''
    page_count_dict = {}
    for file in os.listdir(mypath):
        if file.endswith(".pdf"):
            with open(file, 'rb') as f:
                parser = PDFParser(f)
                book = PDFDocument(parser)
                page_count_dict[file] = resolve1(book.catalog['Pages'])['Count']
            f.close()
    return page_count_dict

def compile_harry_potter_books(path):
    '''
    Coalasces all text from all the Harry Potter series into a single string
    '''
    all_books_text = ""
    for file in os.listdir(mypath):
        if file.endswith(".pdf"):
            with open(file, 'rb') as f:
                raw_parser = parser.from_file(file)
                current_book_text = raw_parser['content']
                all_books_text += " ".join([all_books_text, current_book_text])
            f.close()
    return all_books_text

def read_text():
    '''
    This function reads the harry potter books into python from a directory of pdfs.
    '''
    all_books_text = []
    mypath = os.getcwd()
    for file in os.listdir(mypath):
        if file.endswith(".pdf"):
            with open(file, 'rb') as f:
                parser = PDFParser(f)
                book = PDFDocument(parser)
                all_books_text.append(book)
            f.close()
    return all_books_text

def text_tokenize(book):
    '''
    This function splits words and puctuation in the block of text created in
    the 'read_text' function into one giant list where each item is a word or
    punctuation.

    For example, "Draco hung back for a last word with Severus and
    Regulus." becomes ['Draco', 'hung', 'back', 'for', 'a', 'last', 'word',
    'with', 'Severus', 'and', 'Regulus', '.']
    '''
    tokenize = word_tokenize(book)
    return tokenize

def tagging(tokenize):
    '''
    This function takes the tokenized text created by the text_tokenize function
    and tags each word with a code for the part of speech it represents
    using NLTK's algorithm.  So, it changes the tokenized output:
    ['Crabbe', 'hung', 'back', 'for', 'a', 'last', 'word',
    'with', 'Tom', 'and', 'Goyle', '.']
    - TO -
    [('Crabbe', 'NNP'),
    ('hung', 'VBD'), ('back', 'RP'), ('for', 'IN'), ('a', 'DT'), ('last', 'JJ'),
    ('word', 'NN'), ('with', 'IN'), ('Tom', 'NNP'), ('and', 'CC'),
    ('Goyle', 'NNP'), ('.', '.')]
    '''
    tagged_text = pos_tag(tokenize)
    return tagged_text

def find_proper_nouns(tagged_text):
    '''
    This function takes in the tagged text from the tagging function and returns
    a list of words that were tagged as proper nouns.  It does this by looking
    at the second value in each word/tag pair - e.g. ('Lucius', 'NNP') and determining
    if is is equal to 'NNP'.
    There are a lot of characters in these novels who are referred to with two
    proper nouns, like 'Professor Quirell', 'Mrs. Malfoy', or 'Uncle Vernon',
    and any character can be called by their full name (e.g. 'Salazar Slytherin').
    So, if the second value IS equal to 'NNP', we check the second value of the
    next word - if it is also equal to 'NNP', we string the two words together
    and add them to the proper_nouns list.
    If the second value ISN'T equal to 'NNP', we append (add) only the first
    word to the proper_nouns list.
    As we add nouns to the list, we put them all in lower case - otherwise, our
    program won't know that 'HARRY' is the same thing for our purposes as 'Harry'.
    '''
    proper_nouns = []
    i = 0
    while i < len(tagged_text):
        if tagged_text[i][1] == 'NNP':
            if tagged_text[i+1][1] == 'NNP':
                proper_nouns.append(tagged_text[i][0].lower() +
                                    " " + tagged_text[i+1][0].lower())
                i+=1 # extra increment added to the i counter to skip the next word
            else:
                proper_nouns.append(tagged_text[i][0].lower())
        i+=1 # increment the i counter
    return (proper_nouns)

def summarize_text(proper_nouns, top_num):
    '''
    This function takes the proper_nouns from the list created by the
    find_proper_nouns function and counts the instances of each using
    the most_common method that comes with the counter.
    '''
    counts = dict(Counter(proper_nouns).most_common(top_num))
    return counts

if __name__== "__main__":
    mypath = os.getcwd()
    all_harry_potter_text = compile_harry_potter_books(mypath)
    print(count_pages(mypath))
    # cleaned_hp_string = all_harry_potter_text.translate({ord(i): None for i in '—”’“'})
    tokenized_all_harry_potter = text_tokenize(all_harry_potter_text)
    nltk.download('averaged_perceptron_tagger')
    tagged_all_harry_potter = tagging(tokenized_all_harry_potter)
    proper_nouns_all_harry_potter = find_proper_nouns(tagged_all_harry_potter)
    top_hundred_proper_nouns_all_harry_potter = summarize_text(proper_nouns_all_harry_potter, 100)
    print(top_hundred_proper_nouns_all_harry_potter)

    pickle_out = open("hp_characters.pickle","wb")
    pickle.dump(top_hundred_proper_nouns_all_harry_potter, pickle_out)
    pickle_out.close()
