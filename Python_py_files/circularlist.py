#!/usr/bin/env python
# coding: utf-8

# In[166]:


class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None


# In[167]:


class Circular:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        fin = "["
        temp = self.head
        while temp is not None:
            fin = fin + str(temp.val) + ", "
            temp = temp.next
            if temp == self.head:
                break
                
        fin = fin.rstrip(", ")
        fin = fin + "]"
        return fin


# In[168]:


def get_last(self):
    if self.head is None:
        return None
    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next
    return temp

Circular.get_last = get_last


# In[169]:


def insert(self,index,val):
    new_node = Node(val)
    last = self.get_last()
    
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        
        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node   
        return
    
    if self.head is None:
        raise IndexError("Cannot insert at " + str(index) + " because list is empty.")
    
    temp = self.head
    
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
    prev.next = new_node
    new_node.next = temp
    
Circular.insert = insert  


# In[170]:


def remove(self,val):
    if self.head is None:
        return
    temp = self.head
    last = self.get_last()
    
    if temp.val == val:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    prev = temp
    temp = temp.next
    while temp != self.head:
        if temp.val == val:
            break
        prev = temp
        temp = temp.next
    if temp == self.head:
        return
    prev.next = temp.next
    
Circular.remove = remove


# In[171]:


def pop(self):
    
    last = self.get_last()
    self.remove(last.val)
    return(last.val)
    
Circular.pop = pop


# In[220]:


l = Circular() 
l.insert(0,1)
l.insert(1,2)
l.insert(5,3)
l.insert(3,4)
l.insert(2,5)
l.insert(1,6)
print(l)
#l.remove(2)
#print(l)
last = l.get_last()
print(last.val)
#l.pop()
print(l)
#last = l.get_last()
#print(last.val)
#l.pop()


# In[173]:


def push(self, val):
        new_node = Node(val)
        last = self.get_last()
        
        last.next = new_node
        last.next.next = self.head

Circular.push = push


# In[174]:


l.push(3)


# In[175]:


print(l)
print(l.pop())
print(l)


# In[176]:


def length(self):
    temp = self.head
    count = 0
    
    if temp is None:
        return count
    count = count + 1
    while temp.next != self.head:
        count = count + 1
        temp = temp.next
    return count

Circular.length = length


# In[177]:


l.length()


# In[178]:


def get(self, index):
    temp = self.head
    
    if index == 0:
        return self.head.val
    
    counter = 0
    while temp.next != self.head and counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
        
    return temp.val

Circular.get = get


# In[180]:


l.get(12)


# In[224]:


def remove2(self,index):
    last = self.get_last()
    temp = self.head
    
    if index == 0:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    counter = 0
    while temp.next != self.head and counter < index:
        prev = temp
        temp = temp.next
        counter = counter + 1
    prev.next = temp.next
    
Circular.remove2 = remove2


# In[226]:


print(l)
l.remove2(10)
print(l)


# In[ ]:




