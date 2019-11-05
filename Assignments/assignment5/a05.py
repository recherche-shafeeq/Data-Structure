class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
def __str__(self):
    l = []
    temp = self.head
    while temp is not None:
        l.append(temp.val)
        temp = temp.next
    return(str(l))
LinkedList.__str__ = __str__
def push(self,val):
    new_node = Node(val)
    
    #case:1
    
    if self.head is None:
        self.head = new_node
        return
    
    #case:2
    
    last = self.head
    while last.next is not None:
        last = last.next
    last.next = new_node
    return
LinkedList.push = push
def pop(self):
    if self.head is None:
        raise Exception("Can't Pop.Nothing to pop")
    
    if self.head.next is None:
        val = self.head.val
        self.head = None
        return val
    
    last = self.head
    while last.next is not None:
        prev = last
        last = last.next
    
    val = last.val
    prev.next = None
    return val
LinkedList.pop = pop

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
LinkedList.insert = insert


def remove(self, val):
    temp = self.head
    
    if temp is not None:
        if temp.val == val:
            self.head = temp.next
            temp = None
            return
    
    while temp is not None:
        if temp.val == val:
            break
        
        prev = temp
        temp = temp.next
    if temp is not None:
        prev.next = temp.next
        return
    else:
        prev.next = temp
        return
LinkedList.remove = remove

def len(self):
    count = 0
    temp = self.head
    while temp is not None:
        temp = temp.next
        count += 1
    return count
LinkedList.len = len

def get(self,index):
    if index >= self.len():
        raise IndexError("Index out of bound")
    count = 0
    temp = self.head
    while count < index:
        temp = temp.next
        count += 1
    return temp.val
LinkedList.get = get
def remove_at(self,index):
    if self.head is None:
        raise Exception("Nothing to remove")
    if index >= self.len():
        raise Exception("Not that much elements in the list")
    
    if index == 0:
        self.head = self.head.next
        return
    
    prev = self.head
    temp = prev.next
    counter = 1
    
    while temp.next is not None and counter < index:
        prev = temp
        temp = temp.next
    prev.next = temp.next
LinkedList.remove_at = remove_at

def reverse_list(self):
    if self.head is None or self.head.next is None:
        return
    prev = self.head
    nxt = prev.next
    prev.next = None
    
    while nxt is not None:
        temp_nxt = nxt.next
        nxt.next = prev
        prev = nxt
        nxt = temp_nxt
    self.head = prev
LinkedList.reverse_list = reverse_list

if __name__ == '__main__': 
    l = LinkedList() 
    l.push(1) 
    l.push(2)
    l.push(3)

    print(l)

    l.reverse_list() 
    print(l)

