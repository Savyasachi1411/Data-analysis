#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
df = pd.read_csv ("Netflix Dataset.csv")


# In[9]:


df    # this is our main data frame so we named it "df"


# In[10]:


#BASIC INFO ABOUT OUR DATA


# In[11]:


df.head()                #top 5 records


# In[12]:


df.tail()                   #bottom 5 records


# In[13]:


df.shape                    #(rows,columns)


# In[14]:


df.size                     #Total values in df


# In[15]:


df.columns                 #Show column name


# In[16]:


df.dtypes                #data types of the columns


# In[17]:


df.info()            #Shows info about the df like the indexes the non null values and dtype all in one place


# In[ ]:


#TREATING DUPLICATE VALUES 


# In[19]:


df.head()


# In[22]:


df.shape


# In[23]:


df[df.duplicated()]           #Row wise checking


# In[25]:


df.drop_duplicates(inplace=True)                                # Removing the duplicates 


# In[28]:


df.shape                                                       #Confirming the removal


# In[ ]:


#NULL VALUE CHECKING


# In[29]:


df.isnull()


# In[30]:


df.isnull().sum()


# In[ ]:


#SEABORN HEATMAP


# In[31]:


import seaborn as sns 


# In[32]:


sns.heatmap(df.isnull())


# In[33]:


#LETS DEAL WITH QUESTIONS


# In[ ]:


#Q1 For "House of Cards" what is the show Id and the director name?


# In[38]:


#there are 2 methods
#Method 1

df[df['Title'].isin(['House of Cards'])]


# In[41]:


#Method 2
df[df['Title'].str.contains('House of Cards')]


# In[ ]:


#Question 2 In which year the highest number of tv shows and movies were released? Show with bargraph


# In[42]:


df.dtypes


# In[43]:


df['Date_t'] = pd.to_datetime(df['Release_Date'])


# In[47]:


df.dtypes       #now the date is a datetime64(datatype)


# In[48]:


df['Date_t'].dt.year.value_counts()          #Shows occurance of maximum elements in which Year(Date column)


# In[49]:


df['Date_t'].dt.year.value_counts().plot(kind='bar')                  #Bar Graph for this


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




