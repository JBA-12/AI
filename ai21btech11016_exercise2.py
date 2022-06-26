import string
import numpy as np
import pandas as pd

with open("Doc1.txt","r") as f:
    text=f.read()

a = text.translate(str.maketrans('', '', string.punctuation))
print(a)

a=a.lower()
print(a)

list1 = a.split()
print(list1)



with open("Doc2.txt","r") as f:
    text=f.read()

b = text.translate(str.maketrans('', '', string.punctuation))
print(b)

b=b.lower()
print(b)

list2 = b.split()
print(list2)



with open("Doc3.txt","r") as f:
    text=f.read()

c = text.translate(str.maketrans('', '', string.punctuation))
print(c)

c=c.lower()
print(c)

list3 = c.split()
print(list3)



with open("Doc4.txt","r") as f:
    text=f.read()

d = text.translate(str.maketrans('', '', string.punctuation))
print(d)

d=d.lower()
print(d)

list4 = d.split()
print(list4)


#Vocabulary Building

main_list = list1+list2+list3+list4


main_list = list(set(main_list))

l = len(main_list)
print("The total number of words in vocabulary is", l)



#Creating Dictionary with keys are the tokens in the vocabulary and the value is the 
frequency of that token in the corresponding review

df = pd.value_counts(np.array(list1))
l1 = list(df.values)

dict1 = {list1[i]: l1[i] for i in range(len(list1))}
print(dict1)

df = pd.value_counts(np.array(list2))
l2 = list(df.values)

dict2 = {list2[i]: l2[i] for i in range(len(list2))}
print(dict2)


df = pd.value_counts(np.array(list3))
l3 = list(df.values)

dict3 = {list3[i]: l3[i] for i in range(len(list3))}
print(dict3)


df = pd.value_counts(np.array(list4))
l4 = list(df.values)

dict4 = {list4[i]: l4[i] for i in range(len(list4))}
print(dict4)



#Combining all the dictionary information into a single dataframe 

final = pd.DataFrame({'dict1':pd.Series(dict1),'dict2':pd.Series(dict2), 'dict3':pd.Series(dict3), 'dict4':pd.Series(dict4)})

print(final.T)
