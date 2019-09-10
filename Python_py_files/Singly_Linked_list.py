#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        print("just printing something")
        
    def pop(self):
        
        if self.head is None:
            raise Exception("Can't Pop.Nothing to pop")
            
        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val
        last = self.head
        
        while last is not None:
            self.prev = last
            last = last.next
        self.prev.next = new_node
        new_node.next = last


# In[45]:


def push(self,val):
    new_node = Node(5)
    
    #case:1
    
    if self.head is None:
        head = new_node
        return
    
    #case:2
    
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
    return
Linkedlist.push = push


# In[2]:


def pop(self):
    if self.head is None:
        raise Exception("Can't Pop.Nothing to pop")
    if self.head.next is None:
        val = self.head.val
        self.head = None
        return val
    last = self.head
    while last is not None:
        self.prev = last
        last = last.next
    self.prev.next = new_node
    new_node.next = last
Linkedlist.pop = pop


# In[3]:


l = Linkedlist
#l.pop()


# In[4]:


l.push(4,6)


# In[5]:


l


# In[6]:


l.__init__()


# In[ ]:




