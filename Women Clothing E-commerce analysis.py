#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[27]:


pip install wordcloud


# In[2]:


data=pd.read_csv('Womens Clothing E-Commerce Reviews.csv')
data


# In[5]:


data.duplicated()


# In[6]:


data.isna().sum()


# In[7]:


data=data.dropna()
data


# In[8]:


grouped_data=data.groupby(['Department Name','Age']).size().reset_index(name='Count')
#pivot_table=grouped_data.pivot_table(index='Department Name',columns='Age',values='Count',fill_value=0)
plt.figure(figsize=(12,6))
sns.barplot(x='Department Name',y='Count',data=grouped_data,palette='viridis')
plt.title('Cloth Type Purchases by Age Group')
plt.xlabel('Department Name')
plt.ylabel('Age')
#plt.legend(title='Age')
plt.show()


# In[9]:


sns.countplot(data=data,x='Rating')


# In[ ]:





# In[37]:


pip install textblob


# In[10]:


from textblob import TextBlob
def textblob_women_clothing_analysis(Review):
    sentiment=TextBlob(Review).sentiment
    if sentiment.polarity>0.1:
        return 'Positive'
    if sentiment.polarity<-0.1:
        return 'negative'
    else:
        return 'Neutral'
data['sentiment']=data['Review Text'].apply(textblob_women_clothing_analysis)
data.head()


# In[17]:


sentiment_distribution=data['sentiment'].value_counts()
sentiment_distribution.plot(kind='bar',ylabel='Count',xlabel='Sentiment',title='Distribution of sentiment')
plt.show()


# In[25]:


sns.countplot(data=data,x='Rating',hue='sentiment')
plt.title('Sentiment Distribution Across Ratings')
plt.show()


# In[ ]:


from wordcloud import WordCloud
def generate_word_cloud(Sentiments):
    text=' '.join(review)

