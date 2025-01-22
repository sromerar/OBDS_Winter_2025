#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Create integer, string & boolean variables and print them to the screen
Integer = 5
String = 'Hello'
Boolean = True


# In[6]:


# Verify
type(Integer)


# In[5]:


# Verify
type(String)


# In[7]:


# Verify
type(Boolean)


# In[11]:


# 2. Print the first 10 positive integers using a while loop
i = 1
while i <= 10:
    print(i)
    i = i + 1


# In[9]:


# 3. Print the first 10 negative numbers using a for loop and range function
for i in range (-10,0):
    print(i)


# In[15]:


# 4. Calculate the sum of all numbers between 1 and 10
total = sum(range(1, 11))
print(total)


# In[24]:


# 5. Optional: Print the all the prime numbers under 50

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(2, 50):
    if is_prime(num):
        print(num)

