#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Read presents' dimensions from a file
with open('/Users/madelinebloomberg/Desktop/wrapping_input.txt', 'r') as file:
    presents = [tuple(map(int, line.strip().split('x'))) for line in file]


# In[2]:


#Part 1

def wrapping(dimensions):
    surface_area = 2 * dimensions[0] * dimensions[1] + 2 * dimensions[1] * dimensions[2] + 2 * dimensions[2] * dimensions[0]
    smallest_side = min(dimensions[0] * dimensions[1], dimensions[1] * dimensions[2], dimensions[2] * dimensions[0])
    total_paper = surface_area + smallest_side
    return total_paper


# In[3]:


total_square_feet = sum(wrapping(present) for present in presents)
print("Total square feet of wrapping paper needed:", total_square_feet)


# In[6]:


#Part 2

def calculate_ribbon_needed(dimensions):
    smallest_perimeter = min(2 * (dimensions[0] + dimensions[1]), 2 * (dimensions[1] + dimensions[2]), 2 * (dimensions[2] + dimensions[0]))
    bow_ribbon = dimensions[0] * dimensions[1] * dimensions[2]
    total_ribbon_needed = smallest_perimeter + bow_ribbon
    return total_ribbon_needed


# In[7]:


total_ribbon_feet = sum(calculate_ribbon_needed(present) for present in presents)
print("Total feet of ribbon needed:", total_ribbon_feet)

