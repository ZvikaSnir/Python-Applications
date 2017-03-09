
# coding: utf-8

# In[1]:

import os
os.listdir()


# In[2]:

import pandas


# In[8]:

df1=pandas.read_csv("supermarkets.csv")
df1.set_index("ID")


# In[12]:

df2=pandas.read_json("supermarkets.json")
df2.set_index("ID")


# In[16]:

df3=pandas.read_excel("supermarkets.xlsx",sheetname=0)
df3


# In[18]:

df4=pandas.read_csv("supermarkets-commas.txt")
df4


# In[24]:

df5=pandas.read_csv("supermarkets-semi-colons.txt",sep=";")
df5


# In[43]:

df6=pandas.read_csv("http://pythonhow.com/supermarkets.csv")
df6


# In[59]:

df2=df2.set_index("Address")
df2


# In[ ]:

df2.loc["735 Dolores St":"332 Hill St","Country":"ID"]


# In[68]:

df2.loc[:,"Country"]


# In[73]:

list(df2.loc[:,"Country"])


# In[74]:

df2


# In[75]:

df2.iloc[1:3,1:3]


# In[78]:

df2.ix[3,"Name"]


# In[87]:

df2.drop(df2.columns[0:3],1)


# In[105]:

df2


# In[104]:

len(df2.index)
df2.shape


# In[106]:

df2["Continent"]=df2.shape[0]*["North America"]
df2


# In[109]:

df2["Continent"]=df2["Country"]+","+"North America"
df2


# In[110]:

df2_t = df2.T


# In[111]:

df2_t


# In[116]:

df2_t["My Address"]=["My City","MY Country",10,7,"My Shop","My State","My Continent"]
df2_t
df2 = df2_t.T
df2


# In[117]:

dm=pandas.merge(left=df2,right=df3,on="ID")


# In[118]:

dm


# In[119]:

type(df3)


# In[1]:

from geopy.geocoders import Nominatim


# In[6]:

nom=Nominatim()


# In[17]:

n=nom.geocode("125 Sierra Mesa Dr, San Jose, CA 95116")


# In[20]:

type(n)


# In[22]:

import pandas
df=pandas.read_csv("supermarkets.csv")
df


# In[25]:

df["Address"]=df["Address"]+", "+df["City"] +", "+ df["State"]+ ", "+ df["Country"]
df


# In[26]:

df["Coordinates"]=df["Address"].apply(nom.geocode)


# In[29]:

df


# In[30]:

df.Coordinates[0]


# In[33]:

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)


# In[34]:

df


# In[35]:

df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)


# In[36]:

df


# In[ ]:



