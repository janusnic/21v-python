
# coding: utf-8

# ## Tutorial Setup

# ### Check your install

# In[55]:

import numpy


# In[56]:

import scipy


# In[57]:

import matplotlib


# In[58]:

import sklearn


# In[59]:

import psutil


# In[60]:

import pandas


# In[61]:

import IPython.parallel


# Finding the location of an installed package and its version:

# In[62]:

numpy.__path__


# In[63]:

numpy.__version__


# ### Check that you have the datasets

# In[64]:

get_ipython().magic(u'run ../fetch_data.py')


# In[1]:

import os
for fname in os.listdir('../datasets/'):
    print(fname)


# ## A NumPy primer

# ### NumPy array dtypes and shapes

# In[2]:

import numpy as np


# In[3]:

a = np.array([1, 2, 3])


# In[4]:

a


# In[5]:

b = np.array([[0, 2, 4], [1, 3, 5]])


# In[6]:

b


# In[7]:

b.shape


# In[8]:

b.dtype


# In[9]:

a.shape


# In[10]:

a.dtype


# In[11]:

np.zeros(5)


# In[12]:

np.ones(shape=(3, 4), dtype=np.int32)


# ### Common array operations

# In[13]:

c = b * 0.5


# In[14]:

c


# In[15]:

c.shape


# In[16]:

c.dtype


# In[17]:

a


# In[18]:

d = a + c


# In[19]:

d


# In[20]:

d[0]


# In[21]:

d[0, 0]


# In[22]:

d[:, 0]


# In[23]:

d.sum()


# In[24]:

d.mean()


# In[25]:

d.sum(axis=0)


# In[26]:

d.mean(axis=1)


# ### Reshaping and inplace update

# In[27]:

e = np.arange(12)


# In[28]:

e


# In[29]:

f = e.reshape(3, 4)


# In[30]:

f


# In[31]:

e


# In[32]:

e[5:] = 0


# In[33]:

e


# In[34]:

f


# ### Combining arrays

# In[35]:

a


# In[36]:

b


# In[37]:

d


# In[38]:

np.concatenate([a, a, a])


# In[39]:

np.vstack([a, b, d])


# In[40]:

np.hstack([b, d])


# ## A Matplotlib primer

# In[41]:

get_ipython().magic(u'matplotlib inline')


# In[42]:

import matplotlib.pyplot as plt


# In[43]:

x = np.linspace(0, 2, 10)


# In[44]:

x


# In[45]:

plt.plot(x, 'o-');


# In[46]:

plt.plot(x, x, 'o-', label='linear')
plt.plot(x, x ** 2, 'x-', label='quadratic')

plt.legend(loc='best')
plt.title('Linear vs Quadratic progression')
plt.xlabel('Input')
plt.ylabel('Output');


# In[47]:

samples = np.random.normal(loc=1.0, scale=0.5, size=1000)


# In[48]:

samples.shape


# In[49]:

samples.dtype


# In[50]:

samples[:30]


# In[51]:

plt.hist(samples, bins=50);


# In[52]:

samples_1 = np.random.normal(loc=1, scale=.5, size=10000)
samples_2 = np.random.standard_t(df=10, size=10000)


# In[53]:

bins = np.linspace(-3, 3, 50)
_ = plt.hist(samples_1, bins=bins, alpha=0.5, label='samples 1')
_ = plt.hist(samples_2, bins=bins, alpha=0.5, label='samples 2')
plt.legend(loc='upper left');


# In[54]:

plt.scatter(samples_1, samples_2, alpha=0.1);


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



