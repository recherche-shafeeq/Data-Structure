#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_matched(string):
    opening = '([{'
    closing = ')]}'
    mapping = dict(zip(opening,closing))
    
    stack = []
    
    for c in string:
        
        if c not in mapping.keys() and c not in mapping.values():
            continue
        
        if c in mapping.keys():
            stack.append(mapping[c])
            
        elif len(stack) == 0 or c != stack.pop():
            return False
    return len(stack) == 0


# In[5]:


class Stack:
    def __init__(self):
        self.l = []
    def push(self,val):
        self.l.append(val)
    def pop(self):
        return self.l.pop()
    def length(self):
        return len(l)
    def peek(self):
        return self.l[-1]
def is_matched(string):
    opening = '([{'
    closing = ')]}'
    
    
    mapping = dict(zip(opening,closing))
    s = []
    
    for c in string:
        
        if c not in mapping.keys() and c not in mapping.values():
            continue
        
        if c in mapping.keys():
            s.append(mapping[c])
        
        elif len(s) == 0 or c != s.pop():
            return False
    
    return  len(s)== 0


# In[7]:


is_matched("[{}(()]")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[57]:





# In[66]:





# In[67]:





# In[ ]:




