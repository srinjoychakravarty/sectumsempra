import os, pdftotext

path = os.getcwd()
series_houses = {}

for file in os.listdir(path):
    if (file.endswith(".txt") and not ("requirements.txt") in file):

        # Open the file in read mode
        text = open(file, "r")

        # Create an empty dictionary for words in book
        d = dict()

        # Create an outer dictionary for all books
        book_houses = dict()

        # Loop through each line of the file
        for line in text:
            # Remove the leading spaces and newline character
            line = line.strip()

            # Convert the characters in line to
            # lowercase to avoid case mismatch
            line = line.lower()

            # Split the line into words
            words = line.split(" ")

            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1

        # Append the contents of houses in outer dictionary
        for key in list(d.keys()):
            if (key == "gryffindor" or key == "slytherin" or key == "hufflepuff" or key == "ravenclaw"):
                #print(key, ":", d[key])
                book_houses[key] = d[key]
                #outer_d[file] = (key, ":", d[key])

        series_houses[file[:-4]] = book_houses

print(series_houses)
# Print the contents of dictionary
# for key in list(d.keys()):
#     if (key == "gryffindor" or key == "slytherin" or key == "hufflepuff" or key == "ravenclaw"):
#         print(key, ":", d[key])
