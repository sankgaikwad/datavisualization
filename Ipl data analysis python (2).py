#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


data=pd.read_csv(r"C:\Users\hp\Documents\IPL_Matches_2008_2022.csv")


# In[6]:


data.head()


# In[7]:


data.tail()


# In[8]:


data.info()


# In[9]:


data.isnull().sum


# In[10]:


sns.countplot(data['Season'])
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Total matches played each Season', fontsize=10, fontweight='bold')


# In[11]:


WinningTeam=data['WinningTeam'].value_counts()
WinningTeam.reset_index()


# In[12]:


City=data['City'].value_counts()
City.reset_index()
                    


# # top 5 player of the match
# 
# 

# In[13]:


Player_of_Match=data['Player_of_Match'].value_counts()[0:5]
Player_of_Match.reset_index()


# In[14]:


plt.pie(Player_of_Match.values, labels=Player_of_Match.index,labeldistance=1.2, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title('Most player of the match in IPL',fontsize=10)
plt.show()


# In[15]:


TossDecision=data['TossDecision'].value_counts()
TossDecision.reset_index()


# In[18]:


plt.pie(SuperOver.values, labels=SuperOver.index,labeldistance=1.2, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title('superoverin IPL',fontsize=10)
plt.show()


# In[22]:


import seaborn as sns
sns.countplot(data['TossDecision'])
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('TossDecision', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Toss decision', fontsize=10, fontweight='bold')


# In[ ]:




