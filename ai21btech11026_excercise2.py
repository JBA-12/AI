import string
import pandas as pd
import numpy as np

#Excercise-2  1.a
with open("/Users/saanviamrutha/Downloads/Doc1.txt","r") as f:
    text1 = f.read()
    f.close()
with open("/Users/saanviamrutha/Downloads/Doc2.txt", "r") as f:
    text2 = f.read()
    f.close()
with open("/Users/saanviamrutha/Downloads/Doc3.txt", "r") as f:
    text3 = f.read()
    f.close()
with open("/Users/saanviamrutha/Downloads/Doc4.txt", "r") as f:
    text4 = f.read()
    f.close()

string1 = text1.translate(str.maketrans('','',string.punctuation))
print(string1)
string1=string1.lower()
print(string1)
list1 = string1.split()
print(list1)

string2 = text2.translate(str.maketrans('','',string.punctuation))
print(string2)
string2=string2.lower()
print(string2)
list2 = string2.split()
print(list2)

string3 = text3.translate(str.maketrans('','',string.punctuation))
print(string3)
string3=string3.lower()
print(string3)
list3 = string3.split()
print(list3)

string4 = text4.translate(str.maketrans('','',string.punctuation))
print(string4)
string4=string4.lower()
print(string4)
list4 = string4.split()
print(list4)

#Excercise-2  1.b
l = list1+list2+list3+list4
vocabulary = []
[vocabulary.append(x) for x in l if x not in vocabulary]
print(vocabulary)
n = len(vocabulary)
print('Number of words in the vocabulary are',n)

#Excercise-2  2.a
dict1 = {}
for i1 in vocabulary:
    for i1 in list1:
        dict1[i1]=1
    else:
        dict1[i1]=0
print(dict1)

dict2 = {}
for i2 in vocabulary:
    if i2 in list2:
        dict2[i2]=1
    else:
        dict2[i2]=0
print(dict2)

dict3 = {}
for i3 in vocabulary:
    if i3 in list3:
        dict3[i3]=1
    else:
        dict3[i3]=0
print(dict3)

dict4 = {}
for i4 in vocabulary:
    if i4 in list4:
        dict4[i4]=1
    else:
        dict4[i4]=0
print(dict4)

#Excercise-2  2.b
dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()

for i in vocabulary:
    a=string1.count(i)
    dict_1_new={i:a}
    dict1.update(dict_1_new)
    b = string2.count(i)
    dict_2_new = {i: b}
    dict2.update(dict_2_new)
    c = string3.count(i)
    dict_3_new = {i: c}
    dict3.update(dict_3_new)
    d = string4.count(i)
    dict_4_new = {i: d}
    dict4.update(dict_4_new)
dict_big=[]
dict_big.append(dict1)
dict_big.append(dict2)
dict_big.append(dict3)
dict_big.append(dict4)

df=pd.DataFrame(dict_big,index=['1','2','3','4'])
print(df)

#Excercise-2  3
vec={}
vec[0] = np.array(df.iloc[0])
vec[1] = np.array(df.iloc[1])
vec[2] = np.array(df.iloc[2])
vec[3] = np.array(df.iloc[3])

norm={}
norm[0] = np.linalg.norm(vec[0])
norm[1] = np.linalg.norm(vec[1])
norm[2] = np.linalg.norm(vec[2])
norm[3] = np.linalg.norm(vec[3])

mat=[[[0] for i in range(4)] for j in range(4)]
for i in range(4):
    for j in range(4):
        mat[i][j] = vec[i]@vec[j]/(norm[i]*norm[j])
print(mat)










