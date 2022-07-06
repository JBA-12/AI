import re
import numpy as np
from numpy.linalg import norm
import pandas

# STEP1
with open("Doc1.txt") as doc1:
    data1 = doc1.read()

with open("Doc2.txt") as doc2:
    data2 = doc2.read()

with open("Doc3.txt") as doc3:
    data3 = doc3.read()

with open("Doc4.txt") as doc4:
    data4 = doc4.read()



def tokenization(s:str):
    """
        From the string, removes all punctuation then
    convert all alphabets to lowercase and finally
    Transform the strings into lists composed of words
                                                        """
    result = re.sub(r'[^\w\s]', '', s)
    result_lowercase = result.lower()
    list_of_words = result_lowercase.split()
    return (list_of_words)

def Vocabulary_buiding(repeated_list):
    """
        Store words into a single vocabulary set(list), 
           where each token(word) is stored only once
                                                        """
    unique = np.array(repeated_list)
    unique_list = np.unique(unique)
    return unique_list

repeated_vocabulary = tokenization(data1) + tokenization(data2) + tokenization(data3) + tokenization(data4)

vocabulary = Vocabulary_buiding(repeated_vocabulary)
print(f"Total number of words in the vocabulary is {len(vocabulary)}")


# STEP2 : Create a frequency table

def freq_dictionary(data):
    dict = {}
    for token in vocabulary:
        if token in tokenization(data):
            dict[token] = 1
        else:
            dict[token] = 0

    return dict

dict1 = freq_dictionary(data1)
dict2 = freq_dictionary(data2)
dict3 = freq_dictionary(data3)
dict4 = freq_dictionary(data4)


dataframe = pandas.DataFrame(data=[dict1,dict2,dict3,dict4])
print(dataframe)

# STEP3 : Similarity Calculation

def cosSim(a1,a2):
    """
    """
    cosine = np.dot(a1,a2)/(norm(a1)*norm(a2))
    return cosine

# Convert a dataframe to the list of rows i.e. list of lists
listOfdataframe_Rows = dataframe.to_numpy().tolist()

r1 = np.array(listOfdataframe_Rows[0])
r2 = np.array(listOfdataframe_Rows[1])
r3 = np.array(listOfdataframe_Rows[2])
r4 = np.array(listOfdataframe_Rows[3])

# Rounded to 3 decimal places
cosine_12 = round(cosSim(r1,r2),3)
cosine_13 = round(cosSim(r1,r3),3)
cosine_14 = round(cosSim(r1,r4))
cosine_23 = round(cosSim(r2,r3),3)
cosine_24 = round(cosSim(r2,r4))
cosine_34 = round(cosSim(r3,r4))

data = f'1.0 {cosine_12} {cosine_13} {cosine_14}; {cosine_12} 1.0 {cosine_23} {cosine_24}; {cosine_13} {cosine_23} 1.0 {cosine_34} ; {cosine_14} {cosine_24} {cosine_34} 1.0'

# Store it in a square matrix
review_matrix = np.matrix(data)

list_of_cosSim = [cosine_12, cosine_13, cosine_14, cosine_23, cosine_24, cosine_34]
# Sorting in descending order
list_of_cosSim.sort(reverse=True)

print(f'''The top 3 review pairs with highest similarity between them are: 
    cosSim(r1,r2) = {cosine_12} 
    cosSim(r1,r3) = {cosine_13}
    cosSim(r2,r3) = {cosine_23}
        ''')


    





    



    

