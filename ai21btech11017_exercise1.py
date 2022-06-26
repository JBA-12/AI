#Exercise 1

#1-Converting .csv file to dataframe
#df is the dataframe of shopping.csv
import pandas as pd
import re
df = pd.read_csv('shopping.csv')
print(df)

#2-creating dictionary and giving transaction ID's
# changing Nan to 0.0
df = df.fillna(0.0)

#converting dataframe to dictionary
dict1 = df.to_dict(orient = 'split')

#removing zeroes from the dictionary
for i in range(0,9835):
    count = 0
    for j in range(0,33):
        if (dict1['data'][i][count]== 0):
            dict1['data'][i].pop(count)
        else:
            count =count + 1
            
#items is the dictionary of the whole data in .csv file
items = {}
for i in range(0,9835):
    new_dict1 = {f'T{i+1}': dict1['data'][i]}
    items.update(new_dict1)
   
#five_items is the dictionary of the first five transactions in.csv file
five_items={}
for i in range(0,5):
    new_dict = {f'T{i+1}': dict1['data'][i]}
    five_items.update(new_dict)
print(five_items)    

#3 - Replacing the spaces with _ and writing items in lexical order
dict2 = df.to_dict(orient = 'split')   
for i in range(0,9835):
    column = 0
    for n in range(0,33):
        if type(dict2['data'][i][column]) is float:
            dict2['data'][i].pop(column)
        else:    
            dict2['data'][i][column]=re.sub('\s+','_',dict2['data'][i][column])
            column = column + 1
    dict2['data'][i].sort(key=str.lower)
    
for i in range(9835):
    new_dict2 = {f'T{i+1}': dict2['data'][i]}
    items.update(new_dict2)
    
#Data frame after all changes    
final_df=pd.DataFrame.from_dict(items,orient='index')
final_df = final_df.fillna(0.0)


#4  Function for getting items given transaction id's 
def function(transaction_id):
        print(final_df.iloc[transaction_id-1])
function(32)
function(68)
function(78)

#5 frequent one item sets    
all_items = []
for i in range(0,9835):
    for j in final_df.iloc[i]:
        if j not in all_items:
            all_items.append(j)

# Creating dictionary
one_items = {}

for item in all_items:
    count = 0
    for i in range(0,9835):
        if item in final_df.iloc[i]:
                count = count + 1
    one_items.update({item : (count/9835)*100})

#dictionary with keys as threshold support and values as support
threshold_support1 = {}
percentage = [0.5,1,2,3,5,10]

for i in percentage:
    count = 0
    for j in one_items.values():
        if j>=i:
            count = count + 1
    threshold_support1.update({i: count})

print(threshold_support1)

# one itemsets having support@3
support3_1 = []

for i in one_items.keys():
    if one_items[i]>=3:
        support3_1.append(i)

print(support3_1)

# 6-frequent two item sets
two_items = []
n=len(all_items)

for i in range(0,n):
    for j in range(i+1,n):
        two_items.append((all_items[i],all_items[j]))

# support of two item sets as dictionary
two_items_dict = {}
for i in two_items:
        count = 0
        for items in final_df.iloc:
           if i[0] in items and i[1] in items:
            count = count + 1
        two_items_dict.update({i : (count/9835)*100})


# dictionary according to given threshold supports
threshold_support2 = {}

for i in percentage:
    count = 0
    for j in two_items_dict.values():
        if j>=i:
            count =count + 1
    threshold_support2.update({i: count})

print(threshold_support2)


#two item sets having support@3
support3_2 = []

for i in two_items_dict.keys():
    if two_items_dict[i]>=3:
        support3_2.append(i)

print('Support@3 : ',support3_2)
      
