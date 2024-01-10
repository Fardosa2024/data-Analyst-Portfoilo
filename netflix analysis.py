#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


netflix_data=pd.read_csv("Best Movies Netflix.csv")


# In[12]:


# task1 : is their any duplicate in the dataset
netflix_data[netflix_data.duplicated()]


# In[15]:


# task2 any null values
netflix_data.isnull().sum()


# In[17]:


#import seaborn as sea
#sea.heatmap(netflix_data.isnull())


# In[18]:


# Q1 for "Forrest Gump",What is the show id and who is the director of this show
netflix_data.head()


# In[23]:


netflix_data[netflix_data["TITLE"].isin(["Anbe Sivam"])]


# In[24]:


# to show all records of a particular string in any column
netflix_data[netflix_data["TITLE"].str.contains("Anbe Sivam")]


# In[34]:


# in which year the highest number of the tv shows or movies  were released ? show with Bar Graph
netflix_data.head()


# In[28]:


netflix_data["date_N"]=pd.to_datetime(netflix_data["RELEASE_YEAR"])


# In[35]:


netflix_data.head()


# In[33]:


# it counts the occurrence of all individual years in date column
netflix_data["date_N"].dt.year.value_counts()


# In[36]:


netflix_data["date_N"].dt.year.value_counts().plot(kind="bar")


# In[39]:


# question 3 how MAIN_GENRE are in the dataset
#groupby
# TO group all unique items of column and show their count
netflix_data.groupby(["MAIN_GENRE"]).MAIN_GENRE.count()


# In[46]:


# to show the count of all values of all unique of any column 
netflix_data.groupby(["MAIN_GENRE"]).MAIN_GENRE.count().plot(kind="bar")


# In[49]:


# question 4 show only the titles of all tv show that were released in india
netflix_data[netflix_data["MAIN_GENRE"=="documentry"] & (netflix_data["MAIN_PRODUCTION"]=="US")] ["TITLE"]


# In[54]:


netflix_data.head()
netflix_data["MAIN_PRODUCTION"].value_counts()


# In[55]:


netflix_data.head()


# In[56]:


# how many genre were made in us
netflix_data[netflix_data["MAIN_PRODUCTION"]=="US"]


# In[59]:


# what are the difference ratingd defines bt netflix
netflix_data["SCORE"].unique()


# In[71]:


# how many fantasy got a rating of 6.9 in us
netflix_data[(netflix_data["MAIN_GENRE"]=="fantasy")& (netflix_data["MAIN_PRODUCTION"]=="US")] 


# In[78]:


# what is the maximum duration of a movie on netflix
netflix_data["DURATION"].max()


# In[113]:


netflix_data.sort_values(by=["NUMBER_OF_VOTES"], ascending=False)


# In[89]:





# In[ ]:




