# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import csv, os

def word_cloud_generator(path):
    '''
    Ingests each of the 7-part Harry Potter series in csv form and generates a word cloud
    '''
    for file in os.listdir(path):
        if (file.endswith(".csv")):
            # Reads converted harry potter .csv file
            df = pd.read_csv(file, encoding = "latin-1")
            df.columns.values[1] = "CONTENT"
            comment_words = ' '
            stopwords = set(STOPWORDS)
            # iterate through the csv file
            for val in df.CONTENT:
                # typecaste each val to string
                val = str(val)
                # split the value
                tokens = val.split()
                # Converts each token into lowercase
                for i in range(len(tokens)):
                    tokens[i] = tokens[i].lower()
                for words in tokens:
                    comment_words = comment_words + words + ' '
            cleansed_comment_words = comment_words.replace('free', '').replace('tutorial', '').replace('passuneb', '').replace('video', '').replace('nan', '').replace('â', '')
            wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', stopwords = stopwords, min_font_size = 10).generate(cleansed_comment_words)
            # plot the WordCloud image
            plt.figure(figsize = (8, 8), facecolor = None)
            plt.imshow(wordcloud)
            plt.axis("off")
            plt.tight_layout(pad = 0)
            plt.show()

if __name__== "__main__":
    path = os.getcwd()
    word_cloud_generator(path)
