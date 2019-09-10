#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Linkedlist:
    def __init__(self):
        self.head = None
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 


# In[2]:


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


# In[28]:


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
Linked_List.pop = pop
l = LinkedList() 
l.push(5) 
l.push(6) 
l.remove(6)
m = '[5]'
assert str(l).strip() == m


# In[7]:


def insert(self,index,val):
    new_node = Node(val)
    
    #case:1
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        return
    
    #case:2
    
    temp = self.head
    count = 0
    while temp is not None and count < index:
        prev = temp
        temp = temp.next
        count += 1
    new_node.next = temp
    if self.head is not None:
        prev.next = new_node
    else:
        self.head = new_node
Linkedlist.insert = insert


# In[4]:


def remove(self,val):
    temp = self.head
    if temp is not None:
        if temp.val == val:
            self.head = temp.next
            return
    while temp is not None:
        if temp.val ==val:
            break
        prev = temp
        temp = temp.next
    if temp is None:
        return
    prev.next = temp.next
Linkedlist.remove = remove


# In[20]:


def len(self):
    count = 0
    temp = self.head
    print(temp)
    while temp is not None:
        print(temp.val)
        temp = temp.next
        count += 1
    return count
Linkedlist.len = len


# In[13]:


def get(self,index):
    if index >= length():
        raise IndexError("Index out of bound")
    count = 0
    temp = self.head
    while count < index:
        temp = temp.next
        count += 1
    return temp.val
Linkedlist.get = get


# In[21]:


l = Linkedlist()


# In[22]:


l.len()


# In[23]:


l.push(5)


# In[24]:


l.push(9)


# In[25]:


l.len()


# In[26]:


l.pop()


# In[ ]:




