#!/usr/bin/env python
# coding: utf-8

# # Analysing Data

# ## Arranging Our Data Frame 

# ### Importing Libraries

# In[154]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import matplotlib.ticker as ticker


# ### Reading the file by using panda

# In[7]:


ronaldo_data = pd.read_csv("C:/Users/pc/Desktop/Ronaldo_Statistics_Github")


# ### A rough look at our data

# In[8]:


ronaldo_data.head()


# #### I want to rearrange my data frame

# In[9]:


ronaldo_data.index = ronaldo_data.index + 1


# In[10]:


ronaldo_data = ronaldo_data.drop(columns = "Unnamed: 0")


# ## Our Data Frame

# In[23]:


ronaldo_data
# Now it looks better


# ## Let's See How Was His League Career So Far

# In[45]:


# Correlation between his age and the number of goals:
plt.plot(ronaldo_data["Age"], ronaldo_data["Goals"])
plt.xticks(ronaldo_data["Age"])
plt.grid()
plt.show()


# In[176]:


plt.plot(ronaldo_data["Age"], ronaldo_data["Goals per 90min"])
plt.xticks(ronaldo_data["Age"])
plt.grid()
plt.show()
# Similar to the upper graph
# It should be scary for the rival to know that Ronaldo will score at least 1 goal in the match 


# ### Let's check his performances with respect to the clubs

# In[188]:


group_data = ronaldo_data.groupby(['Club']).sum()
group_data = group_data.drop(columns = "Age")


# In[189]:


group_data


# In[152]:


clubs = [club for club in grouped_data.index]

plt.bar(clubs,ronaldo_data.groupby(['Club']).sum()['Goals'])
plt.xticks(clubs)
plt.ylabel('Goals')
plt.xlabel('Clubs')
plt.show()


# In[179]:


plt.bar(clubs,ronaldo_data.groupby(['Club']).sum()['Assists'])
plt.xticks(clubs)
plt.ylabel('Assists')
plt.xlabel('Clubs')
plt.show()


# ### Let's use linear regression model to have an idea about the number of goals he will score

# In[13]:


m, b = np.polyfit(ronaldo_data["Age"], ronaldo_data["Goals"], 1)


# In[14]:


plt.xticks(ronaldo_data["Age"])
plt.plot(ronaldo_data["Age"], ronaldo_data["Goals"], 'o')
plt.plot(ronaldo_data["Age"], m*ronaldo_data["Age"] + b)


# ### Let's use the same to have an idea about the number of assists

# In[178]:


m, b = np.polyfit(ronaldo_data["Age"], ronaldo_data["Assists"], 1)
plt.xticks(ronaldo_data["Age"])
plt.plot(ronaldo_data["Age"], ronaldo_data["Assists"], 'o')
plt.plot(ronaldo_data["Age"], m*ronaldo_data["Age"] + b)


# ### Linear Regression With Marginal Distributions

# In[21]:


sns.jointplot(x="Goals", y="Assists", data=ronaldo_data,
                  kind="reg", truncate = False,
                  color="m", height=7)
# It can be seen that the season when he scored the highest number of his goals, his number of assists is the highest of his career

