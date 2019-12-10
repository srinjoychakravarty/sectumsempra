import os, pdftotext

def convert_pdfs_to_texts(path):
    '''
    Converts all pdfs to text files from the 7-part Harry Potter series
    '''
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            print("Loading your PDF...")
            with open(file, 'rb') as f:
                pdf = pdftotext.PDF(f)

            filename = str(file[:-4]) + ".txt"
            print("Saving all text from " + file + " to a txt file and writing to disk...")
            with open(filename, 'w') as f:
                f.write("\n\n".join(pdf))

if __name__== "__main__":
    path = os.getcwd()
    convert_pdfs_to_texts(path)
