import nltk, pickle, re
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import squarify
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


# Python code to convert into dictionary
def Convert(tup, di):
    di = dict(tup)
    return di

pickle_in = open("hp_proper_nouns.pickle","rb")
nouns_dict = pickle.load(pickle_in)
hp_nouns = sorted(list(nouns_dict.keys()))

long_nouns = [noun for noun in hp_nouns if (len(noun) - noun.count(' ')) > 2]

extra_characters = []
non_names = ["beauxbatons", "christmas", "death eaters", "hes", "hogwarts", "sirius"]
for noun in long_nouns:
    if (noun.endswith('s')):

        if (noun not in non_names):
            extra_characters.append(noun)

extra_characters_dict = {k: nouns_dict[k] for k in extra_characters}

amended_characters_dict = {}
dropped_s_list = []
for extra_character in extra_characters:
    extra_character_value = extra_characters_dict.get(extra_character)
    amended_key = extra_character[:-1]
    if (amended_key != "dursley"):
        dropped_s_list.append(amended_key)
    amended_characters_dict[amended_key] = extra_character_value

original_characters_dict = {k: nouns_dict[k] for k in dropped_s_list}

dudley_dict = {key: value for key, value in nouns_dict.items() if "dudley" in key}
dursley_dict = {key: value for key, value in amended_characters_dict.items() if "dursley" in key}

key = "dudley dursley"
value = dudley_dict.get("dudley") + dursley_dict.get("dursley")
dudley_dursley_dict = {key: value}
del amended_characters_dict['dursley']

sirius_dict = {key: value for key, value in nouns_dict.items() if "sirius" in key}
black_dict = {key: value for key, value in nouns_dict.items() if "black" in key}
key = "sirius black"
value = sirius_dict.get("sirius") + black_dict.get("black")
sirius_black_dict = {key: value}

combined_dict = {k: amended_characters_dict[k] + original_characters_dict[k] for k in amended_characters_dict}

harry_potter_dict = {key: value for key, value in nouns_dict.items() if "harry potter" in key}
potter_dict = {key: value for key, value in nouns_dict.items() if "potter" in key}
weasley_dict = {key: value for key, value in nouns_dict.items() if "weasley" in key and len(key) == 7}
professor_dumbledore_dict = {key: value for key, value in nouns_dict.items() if "professor dumbledore" in key}

combined_dict.update(dudley_dursley_dict)
combined_dict.update(sirius_black_dict)

combined_dict['harry'] += harry_potter_dict['harry potter']
combined_dict['harry'] += potter_dict['potter']
combined_dict['ron'] += weasley_dict['weasley']
combined_dict['dumbledore'] += professor_dumbledore_dict['professor dumbledore']

reduced_wordlist =  [word for word in long_nouns if word not in dropped_s_list]
further_reduced_wordlist = [word for word in reduced_wordlist if word not in extra_characters]

common_nouns = ['azkaban', 'beauxbatons', 'chapter', 'christmas', 'come', 'cup', 'daily prophet', 'death eaters', 'did', 'dont',
'durmstrang', 'get', 'great hall', 'gryffindor', 'hall', 'hes', 'hogwarts', 'ill', 'invisibility cloak', 'ive',
'just', 'magic', 'ministry', 'muggle', 'page', 'professor', 'quidditch', 'slytherin', 'well']

other_characters = [word for word in further_reduced_wordlist if word not in common_nouns]
other_characters_dict = {k: nouns_dict[k] for k in other_characters}

del other_characters_dict['sirius']
del other_characters_dict['black']
del other_characters_dict['harry potter']
del other_characters_dict['potter']
del other_characters_dict['weasley']
del other_characters_dict['dudley']
del other_characters_dict['professor dumbledore']

combined_dict.update(other_characters_dict)

#plt.bar(combined_dict.keys(), combined_dict.values(), color='maroon')
#plt.show()


index_range = list(range(0, 47))


'''
Creating dataframe by converting dict to list of items
'''
harry_potter_dfObj = pd.DataFrame(list(combined_dict.items()), index = index_range, columns=['Name', 'Mentions'])
sorted_hp_dataframe = harry_potter_dfObj.sort_values('Mentions', ascending = False)

#Utilise matplotlib to scale our character mentions between the min and max, then assign this scale to our values.

sorted_hp_dataframe = sorted_hp_dataframe.iloc[:20]
# norm = matplotlib.colors.Normalize(vmin=min(sorted_hp_dataframe.Mentions), vmax=max(sorted_hp_dataframe.Mentions))
# colors = [matplotlib.cm.Blues(norm(value)) for value in sorted_hp_dataframe.Mentions]

#Create our plot and resize it.
# fig = plt.gcf()
# ax = fig.add_subplot()
# fig.set_size_inches(16, 4.5)

#Use squarify to plot our data, label it and add colours. We add an alpha layer to ensure black labels show through
# squarify.plot(label = sorted_hp_dataframe.Name, sizes = sorted_hp_dataframe.Mentions, color = colors, alpha = .6)
# plt.title("Harry Potter Universe", fontsize=23, fontweight="bold")

#Remove our axes and display the plot
#plt.axis('off')
#plt.show()





#Create a list of colours, in order of our teams on the plot)
# CSLcols = ("#FF0000", "#9A050A", "#112987", "#00A4FA", "#FF6600", "#008040", "#004EA1", "#5B0CB3", "#E50211", "#FF0000",
#            "#00519A",  "#75A315", "#E70008", "#E40000", "#C80815", "#FF3300")

#Create the palette with 'sns.color_palette()' and pass our list as an argument
# CSLpalette = sns.color_palette(CSLcols)
#
# fig, ax = plt.subplots()
# fig.set_size_inches(14, 5)
#
# ax = sns.violinplot(x = "Name", y = "Mentions", data = sorted_hp_dataframe)
# plt.show()


#This next line makes our charts show up in the notebook
#%matplotlib inline

# randomColours = ['#034694','#001C58','#5CBFEB','#D00027',
#               '#EF0107','#DA020E','#274488','#ED1A3B',
#                '#000000','#091453','#60223B','#0053A0',
#                '#E03A3E','#1B458F','#000000','#53162f',
#                '#FBEE23','#EF6610','#C92520','#BA1F1A']

# plt.hlines(y = np.arange(1,21), xmin = 0, xmax = sorted_hp_dataframe['Mentions'], color = "skyblue")
# plt.plot(sorted_hp_dataframe['Mentions'], np.arange(1,21), "o")
# plt.yticks(np.arange(1,21), sorted_hp_dataframe['Name'])
# plt.ylabel("Name")
# plt.xlabel("Mentions")
# plt.title("Harry Potter Character Importance")
# plt.show()


# ser = pd.Series(list(combined_dict.values()), index = pd.MultiIndex.from_tuples(combined_dict.keys()))
# print(ser)
#df = ser.unstack()

first_six_characters = take(11, combined_dict.items())
dictionary = {}
first_eleven_characters_dictionary = Convert(first_six_characters, dictionary)
data = pd.Series(first_eleven_characters_dictionary)
heat_map = sns.heatmap(data.to_frame(), xticklabels=False, cmap="Reds")
plt.xlabel("Importance")
plt.ylabel("Character")
plt.show()

#a = np.array(pd.DataFrame.from_dict(combined_dict))
#print(s.values) # a numpy array

#heat_map = sns.heatmap(s.values)


## Output data to file
#sorted_hp_dataframe.to_csv("sorted_mentions_hp_characters.csv")
