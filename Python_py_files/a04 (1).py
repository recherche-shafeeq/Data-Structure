#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Ring:
    def __init__(self):
        self.head = None


# In[3]:


def __str__(self):
    ret_str ='['
    temp=self.head
    while temp is not None:
        ret_str +=str(temp.val)+", "
        temp=temp.next
        
        if temp==self.head:
            break
    ret_str =ret_str.rstrip(", ")
    ret_str+="]"
    return ret_str
Ring.__str__=__str__


# In[47]:


def _get_last(self):
    if self.head is None:
        return self.head
    temp = self.head.next
    while temp.next  != self.head:
         temp = temp.next
    return temp
Ring._get_last = _get_last


# In[5]:


def insert(self,index,data):
    #case:1 Insertion at zero
    last = self._get_last()
    new_node = Node(data)
    if index == 0:
        new_node.next = self.head
        self.head = new_node
        
        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node
        return
    
    if self.head is None:
        raise IndexError("a veery big error")
    #case:2 if Insertion at any other index
    temp = self.head
    counter = 0
    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1
    prev.next = new_node
    new_node.next = temp
Ring.insert = insert


# In[50]:


def remove(self,data):
    #case:1 when no node is present
    if self.head is None:
        return
    
    #case:2 when value is found at zero node
    temp = self.head
    last = self._get_last()
    if temp.data == data:
        print("Inside first if")
        if last == self.head:
            print("emptying list")
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
            print("Inside second if")
        return
    
    #case:3 if value at any other place than in self.head.val
    prev = temp
    temp = temp.next
    while temp != self.head:
        print("Inside while statement")
        if temp.data == data:
            break
        prev = temp
        temp = temp.next
    #case:4 so because we don't need to loop over the whole array again;so if we didn't find it in the first iteration
    # then check 
    if temp == self.head:
        return
    prev.next = temp.next
Ring.remove = remove


# In[51]:


l = Ring()
l.insert(0,5)
l.insert(1,6)


# In[54]:


print(l)


# In[53]:


l.remove(5)


# In[10]:


def len(self):
    counter = 1
    if self.head is None:
        print("case 1")
        return 0
    
    temp = self.head.next
    while temp != self.head:
        temp = temp.next
        counter += 1
    return counter
Ring.len = len


# In[8]:


def get(self,index):
    if self.len() == 0:
        raise IndexError("What are you doing the list is empty")
    counter = 0
    temp = self.head
    while counter < index:
        temp = temp.next
        counter += 1
    return temp.data
Ring.get = get


# In[15]:


def push(self,data):
    index = self.len()
    return self.insert(index,data)
Ring.push = push


# In[22]:


def remove_at(self,index):
    temp = self.head
    last = self._get_last()
    if index == 0:
        if last == self.head:
            self.head = None
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    count = 0
    prev = temp
    temp = temp.next
    while count < index:
        prev = temp
        temp = temp.next
        count += 1
    prev.next = temp.next
    
Ring.remove_at = remove_at


# In[25]:


r.remove_at(0)


# In[34]:


r.insert(4,6)


# In[35]:


r.remove_at(3)


# In[36]:


print(r)


# In[11]:


r = Ring()


# In[18]:


r.remove_at(6)


# In[29]:


print(r)


# In[68]:


l = Ring()
l.push(5)
l.push(6)


# In[70]:


l.remove(5)


# In[71]:


print(l)


# In[73]:


def pop(self):
    if self.head is None:
        print("Noothing to remove")
        return
    data = self._get_last().data
    remove(data)
    return


# In[ ]:




