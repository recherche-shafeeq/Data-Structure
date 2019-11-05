#!/usr/bin/env python
# coding: utf-8

# In[30]:


class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [ None ] * self.size


# In[31]:


def _get_hash(self, key):
    if type(key) is str:
        return len(key) % self.size
    elif type(key) is int:
        return key % self.size
    else:
        tuple_key = key[0]
        print(tuple_key)
        self._get_hash(tuple_key)
HashMap._get_hash = _get_hash


# In[32]:


# def add(self, key, value):
#     key_hash = self._get_hash(key)
#     key_value = [key, value]
    
#     self.map[key_hash] = [ key_value ]
#     return True

# HashMap.add = add


# In[33]:


def get(self, key):
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    raise KeyError(str(key))
HashMap.get = get


# In[34]:


def __str__(self):
    ret = " "
    for i, item in enumerate(self.map):
        if item is not None:
            ret += str(i) + ": " + str(item) + "\n"
    return ret
HashMap.__str__ = __str__


# In[38]:


h = HashMap()


# In[39]:


h.add(17, "Seventeen")
h.add(26, "Twenty Six")
h.add(35, "Thirty Five")
h.add(26, "Twenty Six Updated")
h.add((22, 2), "Hello")


# In[22]:


print(h)


# In[57]:


print(h.get(26))


# In[37]:


def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]
    
    if self.map[key_hash] is None:
        self.map[key_hash] = [key_value]
        return True
    else:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.map[key_hash].append(key_value)
        return True

HashMap.add = add


# In[10]:


def delete(self, key):
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is None:
        return KeyError(str(key))
    
    for i in range(0, len(self.map[key_hash])):
        if self.map[key_hash][i][0] == key:
            self.map[key_hash].pop(i)
            return True
HashMap.delete = delete


# In[11]:


h = HashMap()

h.add('Three', 3)
h.add(17, "Seventeen")
h.add(26, "Twenty Six")
h.add(35, "Thirty Five")
h.add(25, "Twenty Five")
h.add(26, "Twenty Six Updated")
h.add(36, "Thirty Six")
h.add((24,2), 'tuple text')

print(h)

h.delete(17)
print(h)


# In[ ]:





# In[ ]:




