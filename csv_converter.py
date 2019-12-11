import os
import pandas as pd

def convert_txts_to_csvs(path):
    '''
    Converts all text files to comma separated value files in the 7-part Harry Potter series
    '''
    for file in os.listdir(path):
        if (file.endswith(".txt") and file not in "requirements.txt"):
            print("Loading your txt...")
            df = pd.read_fwf(file)
            filename = str(file[:-4]) + ".csv"
            print("Outputting your converted csv...")
            dataframe = df.to_csv(filename)

if __name__== "__main__":
    path = os.getcwd()
    convert_txts_to_csvs(path)
