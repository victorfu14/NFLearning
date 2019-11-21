#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("pbp-2019.csv")
q= data[['Second']]==29
data.shape


# In[2]:


data


# In[3]:


def split(df, OffenseTeam, DefenseTeam, GameID):
    OffensiveStats = df[(df['GameId'] == GameID) & (df['OffenseTeam'] == OffenseTeam)]
    DefenseStats = df[(df['GameId'] == GameID) & (df['OffenseTeam'] == DefenseTeam)]
    
    return OffensiveStats, DefenseStats

gameData = pd.DataFrame()

for i, row in data.iterrows(): 
    OffenseTeam = row['OffenseTeam']
    DefenseTeam = row['DefenseTeam']
    GameID = row['GameId']
    off, defense = split(data, OffenseTeam, DefenseTeam, GameID)
    s = pd.Series(off.mean()[3:].subtract(defense.mean()[3:]))
    s['GameId'] = GameID
    s['DOffenseTeam'] = OffenseTeam
    s['DefenseTeam'] = DefenseTeam
    gameData = gameData.append(s, ignore_index = True)
#     if (i == 100):
#         break
#     if (i % 1000 == 0):
#         print(off.mean() - defense.mean())
    
# off.mean() - defense.mean()

gameData = gameData
gameData.groupby('GameId').mean()


# In[17]:



gameData.to_csv('/Users/sunao2000/Untitled Folder/datasett.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[56]:


data[data['OffenseTeam'] == 'ARI'].mean()


# In[63]:


data[(data['OffenseTeam'] == 'NE') & (data['DefenseTeam'] == 'NYJ')]


# In[10]:


data1


# In[ ]:





# In[ ]:





# In[3]:


import pandas as pd
data1=pd.read_csv("datasett.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




