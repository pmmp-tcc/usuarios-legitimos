#!/usr/bin/env python
# coding: utf-8

# In[96]:


from secret import *


# In[97]:


id = 61843152


# In[98]:


tweets = list()


# In[99]:


for tweet in client(12).get_users_tweets(id=id, exclude='replies', max_results=100)[0]:
    tweets.append(tweet['id'])
    print(tweet['text'])


# In[100]:


tweets


# In[101]:


users = list()
aux = list()


# In[102]:


import time
i = 1
while len(users) <= 200:
    print(tweets[i])
    if len(users) == 0:
        for user in client(12).get_liking_users(id=tweets[i])[0]:
            users.append(user['id'])
            
        i += 1
    else:
        try:
            for user in client(12).get_liking_users(id=tweets[i])[0]:
                if user['id'] not in users:
                    users.append(user['id'])
            i += 1
        except TypeError:
            i += 1
    time.sleep(1)


# In[103]:


len(users)


# In[104]:


from random import sample


# In[105]:


n = 200


# In[106]:


users = sample(users, n)


# In[107]:


archive = open('Usuarios_camaradeputados.txt', 'a')


# In[108]:


for i in users:
    aux.append(str(i) + '\n')


# In[109]:


archive.writelines(aux)
archive.close()


# In[ ]:





# In[ ]:




