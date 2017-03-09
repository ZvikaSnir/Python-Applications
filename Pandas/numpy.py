
# coding: utf-8

# In[14]:

[[123,123,123,12,13],[123,123,123,12,13],[123,123,123,12,13]]


# In[13]:

import numpy


# In[15]:

n=numpy.arange(27)
n.reshape(3,9)


# In[16]:

n.reshape(3,3,3)


# In[17]:

m=numpy.asarray([[123,123,123,12,13],[],[]])
m


# In[18]:

import cv2


# In[19]:

img = cv2.imread('smallgray.png',0)
img


# In[20]:

cv2.imwrite("newsmallgray.png",img)


# In[21]:

img[0:2,2:4]


# In[22]:

img.shape


# In[23]:

for i in img:
    print(i)


# In[24]:

for i in img.flat:
    print(i)


# In[25]:

img


# In[30]:

ims=numpy.hstack((img,img))
ims


# In[34]:

lst=numpy.hsplit(ims,5)
lst


# In[36]:

lst=numpy.vsplit(ims,3)
lst


# In[ ]:



