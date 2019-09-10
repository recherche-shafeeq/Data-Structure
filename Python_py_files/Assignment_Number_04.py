#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Node:

    def __init__(self,data=None):
    	self.val=data
    	self.next=None

class Ring:
    def __init__(self):
    	self.head=None


def get_last(self):
    
    if self.head is None:
        return None
    
    temp=self.head
    while temp.next!=self.head:
        temp=temp.next
    var=temp.val   
    return temp
Ring.get_last=get_last
def __str__(self):
    re_str="["
    temp=self.head
    
    while temp is not None:
        re_str+=" "+str(temp.val)+", "
        temp=temp.next
        if temp==self.head:
            break
    re_str=re_str.rstrip(",")
    re_str+="]"
    return re_str
Ring.__str__=__str__


def insert(self,index,val):
    
    new_node=Node(val)
    last=self.get_last()
    
        
    if index==0:
        new_node.next=self.head
        self.head=new_node
        
        if last is None:
            self.head.next=self.head
        else:
            last.next=self.head
            
        return
    
    

            
    if self.head is None:
        raise Exception("List is Empty ")
        
    temp=self.head
    count=0
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
    pre.next=new_node
    new_node.next=temp
    
    return
Ring.insert=insert

def len(self):
    
    if self.head is None:
        return 0
    
    temp=self.head
    count=1
    last=self.get_last()
    while temp!=last:
        temp=temp.next
        count+=1
    return count
Ring.len=len
def push(self,val):
    new_node=Node(val)
    
    last=self.get_last()
    
    
    if last is None:
        new_node.next=self.head
        self.head=new_node
        return
    else:
        last.next=new_node
        new_node.next=self.head

Ring.push=push

def remove(self,index):
    
    last=self.get_last()
    temp=self.head
    
    
    if self.head is None:
        return None
    
    if index==0:
        if self.head == self.get_last():
            self.head=None
        else:
            print("case")
            self.head=temp.next
            last.next=self.head
        return
    temp=self.head
    count=0
    while temp!=self.head: 
        pre=temp
        temp=temp.next
        count+=1
        if count==index:
            pre.next=temp.next
            return
Ring.remove=remove

def pop(self):
    last=self.len()-1
    dele=self.remove(last)
    last_element=self.get_last()
    return last_element.val

Ring.pop=pop

def get(self,index):
    
    
    if self.head is None:
        raise IndexError("List is empty")
    if index==0:
        return self.head.val
    
    temp=self.head
    count=0
    while temp is not None and count<index:
        pre=temp
        temp=temp.next
        count+=1
        if temp.val==count:
            break
    return temp.val
    
Ring.get=get    


# In[87]:





# In[3]:


r = Ring()


# In[5]:


r.push(4)


# In[8]:


def push(self,val):
    new_node=Node(val)
    
    last=self.get_last()
    
    
    if last is None:
        new_node.next=self.head
        self.head=new_node
        return
    else:
        last.next=new_node
        new_node.next=self.head

Ring.push=push


# In[77]:


if __name__ == '__main__': 
    r = Ring()
    #r.insert(1, 1)
    #r.insert(0, 1)
    #r.insert(1, 2)
    #r.insert(2, 3)
    #r.insert(3, 5)  # different behavrior since it's a ring! 
    print(r)
    print(r.get_last())
    #print("Lenght : ",r.len())
    #r.push(9)
    #print("Lenght : ",r.len())
    #r.pop()
    #print("after pop : ",r.len())
    #print("case 1 : ",r)
    #r.remove(4)
    #print(r.pop())
    #print(r.get(9))
    
    print(r)


# In[42]:





# In[54]:





# In[59]:





# In[ ]:





# In[ ]:




