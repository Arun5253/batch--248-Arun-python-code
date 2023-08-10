#!/usr/bin/env python
# coding: utf-8

#  ### Basic numeric datatypes -- int, float,complex 

# In[59]:


x = 10.101
print(x,type(x))
# type casting------>changing the value's type
 
x = int(x)
print(x,type(x)) 

x = '5'
print(x,type(x))

x= int(5)
print(x,type(x))

x = 5
x = float(x)
print(x,type(x))


# In[60]:


x =5-3j
print(x,type(x))
# x = int(x)  #uncomment to see code 
x.real , x.imag



# ## bin,oct & hex

# In[61]:


###  bin----------->binary 
x = 17
print(x, type(x))

x = bin(x)
print(x,type(x))


# In[62]:


### oct()
x = 17
print(x, type(x))

x = oct(x)
print(x,type(x))


# In[63]:


#### hex()-----16
x = 17
print(x, type(x))

x = hex(x)
print(x,type(x))


# In[64]:


'''
x = 17
print(x, type(x))

x = oct(x)
print(x,type(x))
''' ### uncomment to see the error


# ### converting bin ,oct, hex values to int  

# In[27]:


int('0x11',0),int('011',16)
help(int)


# In[37]:


x= 3
print(x, type(x))

x = bin(x)
print(x,type(x))
x = 3
print(x, type(x))

x = oct(x)
print(x,type(x))
x= 3
print(x, type(x))

x = hex(x)
print(x,type(x))


# In[54]:


int('0b11',0),int('011',2)
int('0o3',0),int('03',8)
int('0x3',0),int('03',16)


# ## int() with user defined bases
# 

# In[58]:


int('0011',3),int('0011',17),int('0011',32)


# In[ ]:


int('0011',3),int('0011',17),int('0011',32),int('0011',37)#### uncomment

