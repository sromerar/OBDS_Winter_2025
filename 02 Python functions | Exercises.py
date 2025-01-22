#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 1. Write a function to return the complement of a DNA sequence

def complement_sequence(sequence):
    output = ''
    for base in sequence:
        if base == 'A':
            output += 'T'
        elif base == 'G':
            output += 'C'
        elif base == 'C':
            output += 'G'
        elif base == 'T':
            output += 'A'
        else:
            print("Unknown sequence")
    return output

sequence = 'AAAACCCGG'

complement = complement_sequence(sequence)

print(complement)


# In[20]:


# 2. Write a function to reverse a string

def reverse_string(s):
    return s[::-1]


# In[21]:


# Validation

string = "hello"
reversed_string = reverse_string(string)
print(reversed_string) 


# In[23]:


# 3. Write a function to return the reverse complement of a sequence

def reverse(s):
    return s[::-1]

reverse_complement = reverse(complement)

print(reverse_complement)

