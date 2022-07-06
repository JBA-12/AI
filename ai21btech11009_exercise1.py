import string
import pandas as pd
import re
N_TOTAL = 9835

def underscore(s):

    # Replace all instances of whitespace with a single dash "_"
    s = re.sub(r"\s+", '_', s)
    return s

df = pd.read_csv('shopping.csv')
numpy_2d_array = df.to_numpy()
listOfDFRows = numpy_2d_array.tolist()

list2 = []
list_of_items_purchased = []
 
for i in listOfDFRows:
    list1 = []
    list2 = []
    for j in range(int(i[0])):
        list1 = list2.append(i[j+1])

    list_of_items_purchased.append(list2)

dict = {}
# Formatting it to a dict where the {key:value} corresponds to Transaction Id
# and the corresponding list of items purchased respectively
i = 1
for inner_list in list_of_items_purchased:
    dict[f"T{i}"] = inner_list
    i += 1

# Printing the first five key value pairs : first5pairs is a dictionary 
first5pairs = {k: dict[k] for k in list(dict)[:5]}
print(first5pairs)

# STEP 3 : converting the name of all items to a single underscore format 
# and sorting them
for key in dict:
    i  = 0
    for item in dict[key]:
        dict[key][i] = underscore(item)
        i+=1
    dict[key].sort()

# STEP 4: Printing all the items for transaction IDs 32, 68, 78
def transactionID(ID: string):
    """ 
        takes a transaction ID as an input argument 
        prints all the items purchased in that transaction
                                                            """
    print(f"TID{ID}: Items purchased -")
    for item in dict[ID]:
        print(item)


# transactionID("T32")
# transactionID("T68")
# transactionID("T78")

# STEP 5 :
fruit_list = []
# fruit_list contains duplicate items too
for key in dict:
    fruit_list += dict[key]


def support_calculator(freq_dict):
    """ 
    Takes a frequency dictionary {key:value} where key
     is the fruit and value the freq AND returns another dict 
    where key = fruit and value is the support of the item
                                                                """
    support_dict = {}
    for key in freq_dict:
        support_dict[key] =(freq_dict[key]/N_TOTAL) * 100

    return support_dict

def frequency_calculator(my_list):
    """
    Takes a list as an argument and 
    computes the frequency of each item in the list.
                                                     """
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    
    return(freq)

def is_frequent(support_dict:dict,percent:int):
    """
    takes a dictionary whose key:value pairs are 
    fruit:support and returns a list containing 
    only the fruits whose support > given support threshold
                                                            """
    list_of_frequent_items = []
    for key in support_dict:
        if support_dict[key] > percent:
            list_of_frequent_items.append(key)
    
    return (list_of_frequent_items)


freq_dict = frequency_calculator(fruit_list)
unique_fruit_list = []
for key in freq_dict:
    unique_fruit_list.append(key)

support_dict = support_calculator(freq_dict)
list_of_support_3 = is_frequent(support_dict,3)
print(list_of_support_3)



#  STEP 6:
two_pair = []


for i in range(len(unique_fruit_list)):
    for j in range(i+1,len(unique_fruit_list)):
        two_pair.append((unique_fruit_list[i],unique_fruit_list[j]))

# Creating and appending two_item dictionary key as itemsets and value as support.
two_itemset_with_support_value = {}

for item in two_pair:
    count = 0
    # tapping into each rows(transaction detail) and checking if both items in the tuple is present or not
    for lst in list_of_items_purchased:
        if item[0] in lst and item[1] in lst:
            count += 1
    newdict = {item : (count/N_TOTAL)*100}
    two_itemset_with_support_value.update(newdict)


# Creating threshold_support dictionary to store the support value and No.of items .
Threshold_support_twoitm = {'support' : 'No. of items'}

percent_list = [0.5,1,2,3,5,10]

# prints out support@3 items
print("support@3 :")
for percent in percent_list:
    count = 0
    for itemset, support in two_itemset_with_support_value.items():
        if support>percent:
            count += 1
            if percent == 3:
                print(f"{itemset}")

    newdict = {f'support@{percent}': count}
    Threshold_support_twoitm.update(newdict)

# Printing support and No.of items.
print(list(Threshold_support_twoitm.keys()))
print(list(Threshold_support_twoitm.values()))




    

    



    

 


    

