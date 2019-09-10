#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


# In[2]:


class Doubly:
    def __init__(self):
        self.head = None


# In[7]:


def push(self,data):
    new_node = Node(data)
    #no nodes
    if self.head is None:
        self.head = new_node
        return
    #one or more than one nodes
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
    new_node.prev = last
Doubly.push = push


# In[22]:


d = Doubly()


# In[46]:


d.push(6)


# In[47]:


d.push(5)


# In[31]:


def __str__(self):
    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str += str(temp.data) + ', '
        temp = temp.next
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str
Doubly.__str__ = __str__


# In[32]:


print(d)


# In[43]:


def pop(self):
    if self.head is None:
        raise Exception('Nothing to pop')
    
    if self.head.next is None:
        data = self.head.data
        self.head = None
        return data
    
    last = self.head
    while last.next is not None:
        prev = last
        last = last.next
    data = last.data
    prev.next = None
    return data


# In[44]:


Doubly.pop = pop


# In[50]:


d.pop()


# In[52]:


def insert(self,index,data):
    new_node = Node(data)
    
    if index == 0:
        new_node.next = self.head
        if sself.head is not None:
            self.prev = new_node
        self.head = new_node
    if temp
    counter = 0
    temp = self.head
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        
    prev.next = new_node
    new_node.prev = prev
    new_node.next = temp
    if temp is not None:
        temp.prev = new_node
Doubly.insert = insert


# In[89]:


d = Doubly()


# In[92]:


d.push(11)


# In[93]:


d.push(81)


# In[60]:


d.pop()


# In[61]:


d.insert(5,6)


# In[81]:


def remove(self,data):
    if self.head is None:
        raise Exception("Nothing to remove")
    if self.head is not None:
        if self.head.data == data:
            self.head = None
    prev = self.head
    temp = prev.next
    while temp is not None:
        if temp.data == data:
            break
        prev = temp
        temp = temp.next
    if temp is None:
        print("value not found")
        return
    prev.next = temp.next
    prev.next.prev = prev
Doubly.remove = remove


# In[95]:


d.remove(81)


# In[96]:


print(d)


# In[71]:


str(d)


# In[72]:


d


# In[ ]:




