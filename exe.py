import pandas as pd

df = pd.read_csv('us.csv')

#deleting year col
del df['Year']

df['avg']=df.mean(1)

#print(df)

lt=[]
for i in range(0,72):
   k = 1948+i
   lt.append(k)
   
for i in range(0,72):
   df.loc[i,'Year'] = str(lt[i])

xy=df.pop('Year')
df.insert(0,'Year',xy)

print(df)