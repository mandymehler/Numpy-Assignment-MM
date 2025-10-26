#!/usr/bin/env python
# coding: utf-8

# In[15]:


#QUESTION 1 
#Import numpy and print version. 

import numpy as np

print("current numpy version is:", (np.__version__))


# In[19]:


#QUESTION 2
#Create a 1D array of numbers from 0 to 9. 
#Desired output: #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

import numpy as np

arr = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9]) #manually

arr_use_arange = np.arange(10) #using np.arange, creates array evenly spaced, stop is 10
#no start or step so defaults to 0 and 1

print(arr)
print(arr_use_arange)


# In[6]:


#QUESTION 3
#Import a dataset with numbers and texts keeping the text intact in python numpy. 
#Use the iris dataset available (URL below)

import numpy as np

# URL of the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Import dataset with text intact
# delimiter = "," comma-separated (CSV file) #I looked this up and used .Sniffer to check
# dtype=None has both numbers and text or can use object
# encoding='utf-8' character format almost always this. It handles normal English + special characters

data = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')
print(data)


# In[8]:


#PROBLEM 4 Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. 
#Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)

#Option 1 - (using numpy.where)

#First convert to numeric array since we are looking for petal width float (>1.0)
import numpy as np 

petal_array = np.array([row[3] for row in data], dtype=float) #convert 4th column(index 3) 

petal_width = petal_array > 1.0

array_pwg = np.where(petal_width)[0] #returns a tuple of arrays that contain the indices 
#of the elements that satisfy the condition (or are True) 
#[0]extracts the first array(or row) where the pedal_width is > 1.0 is true

first_index_pwg = array_pwg[0] #0 is the first index

print("First index where petal width is > 1.0:", first_index_pwg1)
print("The value of the first pedal width > 1.0 is:", petal_array[first_index_pwg])


# In[5]:


#PROBLEM 4 - Option 2 (using numpy.argmax)

import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = np.genfromtxt(url, delimiter=",", dtype=None, encoding="utf-8")

# Extract the 4th column, numpy evaluates row by row, so 4th column would be 4th element or 3rd index in each row
# converts data type (petal width) to float
petal_width = np.array([row[3] for row in data], dtype=float)

# Find the first index where petal width > 1.0
index = np.argmax(petal_width > 1.0)

#np.argmax returns the INDEX where the value is > 1.0, not the value.  
pw_value = petal_width[index]


print("First occurrence index is:", index)
print("The value of the first pedal width > 1.0 is:", pw_value)


# In[16]:


#5 PROBLEM 5 - Option 1 (use for loop)
import numpy as np

np.random.seed(100) #sets up random generator, seed will produce the same sequence of random numbers 
#100 is the seed value. It is a starting point. It somewhat "labels" the generator. 

a = np.random.uniform(1, 50, 20)
#generates 20 random numbers with equal probability between 1 and 50
#returns a 1D numpy array in a 

# Loop through each element of array at index i
for i in range(len(a)):
    if a[i] > 30: #if greater than 30
        a[i] = 30 #equals 30
    elif a[i] < 10: #else if less than 10
        a[i] = 10 #replace with 10
        #the remaining index values between 10 and 30 will stay the same

print(a)


# In[9]:


#PROBLEM 5 - Option 2 use numpy.clip
#syntax np.clip(array, min_value, max_value)
#values in the array less than min_value are set to min_value
#same for max_value but greater than
#values between remain unchanged. 
import numpy as np
np.random.seed(100) 
a = np.random.uniform(1, 50, 20)
a = np.clip(a, 10, 30)
print(a)




# In[ ]:




