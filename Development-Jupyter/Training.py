#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris


# In[2]:


import pandas as pd


# In[3]:


df = load_iris()


# In[13]:


X=pd.DataFrame(data=df['data'],columns=df['feature_names'])


# In[16]:


Y=df['target']


# In[20]:


Y_labels = {0:'setosa', 1:'versicolor', 2:'virginica'}


# In[28]:


Y=pd.Series(Y).map(Y_labels)


# In[29]:


Y.head()


# In[34]:


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(X,Y,random_state=42)


# In[35]:


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=20)


# In[36]:


clf = clf.fit(x_train,y_train)
y_pred = clf.predict(x_test)


# In[37]:


from sklearn import metrics
print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))


# In[39]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)


# In[40]:


import pickle


# In[43]:


pickle.dump(clf, open("..//model//model.sav", 'wb'))


# In[45]:


get_ipython().system('(pip3 freeze > requirements.txt)')


# In[ ]:




