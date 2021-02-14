#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

# univariate analysis to calc MSE (https://www.youtube.com/watch?v=uD1Dfz0aqkA_)
# given values (i.e. marks scored by student) = total 70, mean 14
Y_true = [19,17,9,13,12] # = Y (original values)

#calculated values
Y_pred = 14 #  same as Y [14,14,14,14,14]

# MSE (subtract each value from 14, sqaure them and add them)
MSE = np.square(np.subtract(Y_true,Y_pred)).mean()

print (MSE)


# In[5]:


# we can do all above with formula using sklearn
from sklearn.metrics import mean_squared_error
# given values
Y_true = [19,17,9,13,12] 
# calculated values
# can't use Y_pred = 14 , have to full list in sklearn
Y_pred = [14,14,14,14,14]

#calc of MSE
MSE = mean_squared_error (Y_true, Y_pred)
print (MSE)


# In[ ]:




