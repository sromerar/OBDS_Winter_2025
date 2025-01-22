#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1) Create a list called 'participants' containing the of the names of your fellow trainees

participants = ['Aleema', 'Muyang', 'Sinibaldo', 'Oliver', 'Yi']


# In[2]:


participants


# In[3]:


# 2) Create the following new variables participants_2 and participants_3 by typing:

participants_2 = participants
participants_3 = participants.copy()


# In[4]:


participants_2


# In[5]:


participants_3


# In[6]:


# 3) Add the names of today's trainers to the list 'participants' using append

participants.append('Kevin')
participants.append('David')


# In[7]:


participants


# In[8]:


# 4) Print the 'participants', 'participants_2' and 'participants_3' 
# lists – what do you notice and why does this happen


# In[9]:


participants


# In[10]:


participants_2 


# In[11]:


participants_3


# In[12]:


# 5) Select the 3rd and 5th names from your participants list

selected_names = [participants[2], participants[4]]  
print(selected_names)


# In[13]:


# 7) Select the first 2 letters of the string in the third value of your participants list

third_value = participants[2]
first_two = third_value[:2]
print(first_two)


# In[14]:


participants


# In[15]:


# 8) Iterate over the participants list and set the names to keys in a dictionary with 
# the value as 'trainee’ or ‘trainer’ depending on thier role.

participants = {
    'Aleema': 'trainee', 
    'Muyang': 'trainee',
    'Sinibaldo': 'trainee',
    'Oliver': 'trainee',
    'Yi': 'trainee',
    'Kevin': 'trainer',
    'David': 'trainer'
}

print(participants)


# In[16]:


# 9) Use a for loop to iterate over your dictionary and print the values of the keys only if they are trainees

for participant, role in participants.items():
    if role == 'trainee':
        print(participant)


# In[18]:


# 10) Make a function called 'random_name_generator' that prints the course participants names one 
# by one when prompted in a randomised order each time it is run.

import random

def random_name_generator():
    names = list(participants.keys())  
    random.shuffle(names)  
    for name in names:  
        print(name)

random_name_generator()

