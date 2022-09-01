#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=2
b=3
a,b=b,a
print(a,b)


# In[3]:


print("hajime mashitte")


# prateek desu

# In[7]:


import random 
import numpy as np


# In[17]:


actual_vals=[1]*50+[0]*50
predict_vals= random.choices([0,1],k=100)


# In[18]:


predict_vals[0:10]


# In[20]:


fp=0
fn=0

tp=0
tn=0

for actual_val,predict_val in zip(actual_vals,predict_vals):
    if predict_val==actual_val:
        if predict_val==1:
            tp+=1
        else:
            tn+=1
    else:
        if predict_val==1:
            fp+=1
        else:
            fn+=1
confusion_matrix = [
    [tn,fp],
    [fn,tp]

]
one_confusion_matrix=np.array(confusion_matrix)
one_confusion_matrix


# In[ ]:


import pandas as pd
import seaborn  as sb


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
imoport matplotlib.pyplot as plit
plt.style.use('fivethirtyeight')

y_predict=predict_val
y_actual=actual_val

data={
    'y_predicted':y_predict,
    'y_actual':y_actual
    
}
df=pd.DataFrame


# 
