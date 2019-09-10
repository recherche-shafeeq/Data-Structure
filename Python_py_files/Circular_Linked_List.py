#!/usr/bin/env python
# coding: utf-8

# In[109]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Ring:
    def __init__(self):
        self.head = None


# In[110]:


def __str__(self):
    ret_str = '['
    last = self.head
    while last is not None:
        ret_str += str(last.data) + ', '
        last = last.next
        if last == self.head:
            break
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
    return ret_str
Ring.__str__ = __str__


def _get_last(self):
    if self.head is None:
        return self.head
    last = self.head
    while last.next != self.head:
        last = last.next
    return last
Ring._get_last_node = _get_last_node
def _get_last_val(self):
    if self.head is None:
        print("first case")
        return self.head
    last = self.head
    while last.next != self.head:
        last = last.next
    return last.data
Ring._get_last = _get_last


# In[111]:


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
    return
Ring.insert = insert


# In[112]:


def remove(self,data):
    #case:1 when no node is present
    if self.head is None:
        raise Exception("Nothing to remove")
    
    #case:2 when value is found at zero node
    temp = self.head
    last = self._get_last()
    if temp.data == data:
        if temp.next == self.head:
            self.head = None
            return
        else:
            self.head = self.head.next
            last.next = self.head
            return
    #case:3 if value at any other place than in self.head.val
    prev = temp
    temp = temp.next
    while temp != self.head:
        if temp.data == data:
            break
        prev = temp
        temp = temp.next
    #case:4 so because we don't need to loop over the whole array again;so if we didn't find it in the first iteration
    # then check 
    if temp == self.head:
        raise Exception("Value not found")
        return
    prev.next = temp.next
Ring.remove = remove


# In[182]:


def length(self):
    counter = 1
    if self.head is None:
        print("case 1")
        return 0
    
    temp = self.head.next
    while temp != self.head:
        temp = temp.next
        counter += 1
    return counter
Ring.length = length

def push(self,data):
    self.insert(self.length(),data)
    return
Ring.push = push

def pop(self):
    try:
        print(self._get_last())
        self.remove(self._get_last_val()).data
    except Exception:
        print("value not found")
Ring.pop = pop

def _get_last_node(self):
    last = self.head
    while last.next is not None:
        last = last.next
    return last
Ring._get_last_node = _get_last_node


# In[221]:


h


# In[118]:


r.push(4)


# In[120]:


r.remove(4)


# In[122]:


r.push(4)


# In[125]:





# In[ ]:





# In[ ]:





# In[21]:





# In[23]:





# In[10]:


print(r)
r.insert(1,4)


# In[ ]:





# In[94]:





# In[91]:





# In[92]:





# In[83]:





# In[84]:





# In[ ]:





# In[25]:


print(r)


# In[148]:


r.insert(0,6)


# In[149]:


print(r)


# In[47]:





# In[48]:





# In[54]:


r.get(1)


# In[96]:





# In[205]:





# In[206]:





# In[207]:


r = Ring()


# In[ ]:





# In[216]:


r.insert(0,6)


# In[217]:


r.insert(1,5)


# In[218]:


r.remove(1)


# In[219]:


print(r)


# In[153]:


print(r)


# In[154]:


r.length()


# In[177]:


r.insert(0,1)


# In[178]:


print(r)


# In[179]:


r.insert(2,6)


# In[180]:


print(r)


# In[181]:


r.length()


# In[183]:


r = Ring()


# In[184]:


r.length()


# In[186]:


r.insert(0,4)


# In[187]:


r.length()


# In[ ]:




