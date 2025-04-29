#!/usr/bin/env python
# coding: utf-8

# # Typecasting in Python
# * The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
# * Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# In[27]:


a="5"
b="1"
print(a+b)
#print(type(a),type(b))


# In[28]:


a=5
b=1
print(a+b)
#print(type(a),type(b))


# In[29]:


a="5"
b="1"
print(int(a)+int(b))
#print(type(a),type(b))


# ## Two Types of Typecasting:
# 1. Explicit Conversion (Explicit type casting in python)
# 2. Implicit Conversion (Implicit type casting in python).
# ### Explicit typecasting:
# - The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.
# - It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .
# - Example:

# In[30]:


a="5"#type of a is string
b="1"#type of b is string
print(int(a)+int(b))#Here we converted manualy into integer


# In[31]:


string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


# ### Implicit type casting:
# * Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.
# * Python converts a smaller data type to a higher data type to prevent data loss.

# In[32]:


a=5.9
b=1
print(a+b)


# In[33]:


# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))


# In[ ]:





# In[ ]:





# In[ ]:




