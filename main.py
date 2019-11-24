from tika import parser
raw = parser.from_file('1philosophersstone.pdf')
#print(raw['content'])

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
import os
from os import listdir
from os.path import isfile, join

from nltk import word_tokenize


def count_pages():
    '''
    Count the number of pages in the book
    '''
    page_count_dict = {}
    mypath = os.getcwd()
    for file in os.listdir(mypath):
        if file.endswith(".pdf"):
            with open(file, 'rb') as f:
                parser = PDFParser(f)
                book = PDFDocument(parser)
                page_count_dict[file] = resolve1(book.catalog['Pages'])['Count']
            f.close()
    return page_count_dict


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
                print(file, resolve1(book.catalog['Pages'])['Count'])
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
# mypath = os.getcwd()
# for file in os.listdir(mypath):
#     if file.endswith(".pdf"):
#         opened_file = open(file, 'rb')
#         parser = PDFParser(opened_file)
#         document = PDFDocument(parser)
#         # This will give you the count of pages
#         print(file, resolve1(document.catalog['Pages'])['Count'])


# import nltk
# import nltk.data
# nltk.download('punkt')
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
#
# corpus = nltk.corpus.reader.PlaintextCorpusReader("1philosophersstone.pdf", r'.*', encoding='latin-1')
#fp = open("1philosophersstone.pdf")
#fp = open('1philosophersstone.pdf', encoding = "utf-8")
#job_titles = [line.decode('utf-8').strip() for line in fp.readlines()]
#data = corpus.read()
# print('\n-----\n'.join(tokenizer.tokenize(str(corpus))))
if __name__== "__main__":
    print(count_pages())
    #print(type(read_text()[2]))
