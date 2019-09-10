#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Linkedlist:
    def __init__(self):
        self.head = None
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 


# In[4]:


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


# In[5]:


def pop(self):
    
    if self.head is None:
        raise Exception("Cannot Pop. No value")
    
    if self.head.next is None:
        val = self.head.val
        self.head = None
        return val
    
    temp = self.head
    while temp.next is not None:
        prev = temp
        temp = temp.next
    
    val = temp.val
    prev.next = None
    
    return val


# In[6]:


Linkedlist.pop = pop


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


# In[8]:


l = Linkedlist()


# In[16]:





# In[20]:


l.insert(0,4)
l.insert(1,3)
l.insert(2,22)
l.insert(3,33)
l.insert(4,44)
l.insert(5,55)
l.insert(6,66)


# In[32]:


l.insert(66,55)


# In[33]:


l.pop()


# In[46]:


def length(self):
    count = 0
    temp = self.head
    while temp is not None:
        temp = temp.next
        count += 1
    return count
Linkedlist.length = length


# In[47]:


l.length()


# In[48]:


def get_val(self,index):
    count = 0
    temp = self.head
    while count < index:
        temp = temp.next
        count += 1
    return temp.val


# In[49]:


Linkedlist.get_val = get_val


# In[50]:


l.get_val(3)


# In[51]:


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


# In[52]:


l.remove(55)


# In[6]:


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


# In[5]:


l = Linkedlist
l.pop()


# In[16]:


def __str__(self):
    l = []
    temp = self.head
    while temp is not None:
        l.append(temp.val)
        temp = temp.next
    return(str(l))


# In[17]:


Linkedlist.__str__ = __str__


# In[18]:


l = Linkedlist()


# In[21]:


print(l)


# In[33]:


l.pop()


# In[48]:


def remove(self,val):
    if self.head is None:
        raise Exception("Nothing to remove")
    last = self.head
    if last is not None and last.val == val:
        last = last.next
        return val
    while last is not None:
        self.prev = temp
        temp = temp.next
        if last.val == val:
            break
    if temp is not None:
        prev.next = temp.next
    else:
        prev.next = temp


# In[35]:


Linkedlist.remove = remove


# In[37]:


l = Linkedlist()


# In[46]:


l.insert(7,5)


# In[42]:


print(l)


# In[47]:


l.insert(3,6)


# In[ ]:


l.remove()

