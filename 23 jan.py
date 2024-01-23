#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[5]:


df= sns.load_dataset("iris")


# In[6]:


df


# In[4]:


## Violinplot
## It is similar to the boxplot except that it provides a higher, more advanced visualization and uses the kernel 
##density estimation to give a better description about the data distribution.

sns.violinplot(x='species', y='sepal_width', data=df)
plt.show()


# In[7]:


##Stripplot
## It basically creates a scatter plot based on the category. 
# It is created using the stripplot()
sns.stripplot(x='species', y='petal_width', data=df)
plt.show()


# In[8]:


## Histogram
## A histogram is basically used to represent data provided in a form of some groups.
## It is accurate method for the graphical representation of numerical data 
## distribution
sns.histplot(x='petal_width', data=df)
plt.show()


# In[9]:


sns.histplot(x='petal_width', data=df,hue='species', kde=True) # kernel density estimation 
plt.show()
#kde is approximation of histogram to density curve


# In[10]:


import warnings
warnings.filterwarnings('ignore')
## Distplot
## Distplot is used basically for univariant set of observations
# and visualizes it through a histogram 
## i.e. only one observation and hence we choose one particular column of the dataset
sns.distplot(df['petal_width'],color="g") # ,hist=False, kde=False
plt.show()
## density means the probability of given point to lie on the curve.


# In[11]:


##Pairplot
##Pairplot represents pairwise relation across the entire dataframe and supports an 

## additional  argument called hue for categorical separation. 
#What it does basically is create a jointplot between every possible numerical 
##column and takes a while if the dataframe is really huge

sns.pairplot(data=df, hue='species')
plt.show()


# In[12]:


# categorical plot
sns.catplot(x='sepal_length', data=df, kind='violin')
plt.show()


# In[13]:


sns.catplot(x='petal_length',y='species',data=df)
plt.show()


# In[14]:


## Violinplot
## It is similar to the boxplot except that it provides a higher, more advanced visualization and uses the kernel 
##density estimation to give a better description about the data distribution.

sns.violinplot(x='species', y='sepal_width', data=df)
plt.show()

##Stripplot
## It basically creates a scatter plot based on the category. 
# It is created using the stripplot()
sns.stripplot(x='species', y='petal_width', data=df)
plt.show()



#The default representation of the data in catplot() uses a stripplot
sns.catplot(x='petal_length',y='species',data=df)
plt.show()


# In[ ]:




