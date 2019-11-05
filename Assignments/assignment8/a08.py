class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

def _get_hash(self,key):
    if type(key) == int:
        return key % self.size
    elif type(key) == str:
        asscii = ord(key[0])
        return asscii % self.size
    elif type(key) == tuple:
        return sum(key) % self.size
HashMap._get_hash = _get_hash

def get(self,key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is not None:
        for pair in self.map[key_hash]:
            if pair[0] == key:
                return pair[1]
    raise KeyError(str(key))
HashMap.get = get

def __str__(self):
    ret = ""
    for i,item in enumerate(self.map):
        if item is not None:
            ret += str(i) +": " + str(item) + "\n"
    return ret
HashMap.__str__ = __str__

def add(self,key,value):

    key_hash = self._get_hash(key)
    key_value = [key,value]
    
    if self.map[key_hash] is None:
        self.map[key_hash]= [key_value]
        return True

    else:
        for i in self.map[key_hash]:
            if i[0] == key:
                i[1] = value
                return True
    
    self.map[key_hash].append(key_value)
    return True
HashMap.add = add

def delete(self, key):
    key_hash = self._get_hash(key)
    
    for idx,key_value in enumerate(self.map[key_hash]):
        if key_value[0] == key:
            self.map[key_hash].pop(idx)
            return True
HashMap.delete = delete



if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)
