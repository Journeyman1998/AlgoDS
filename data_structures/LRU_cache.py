
class Node:

    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.list_node = {}
        self.size = 0

        self.head_LRU = Node(-1)
        self.tail_LRU = Node(-1)
        self.head_LRU.next = self.tail_LRU
        self.tail_LRU.prev = self.head_LRU

    def get(self, key):
        if key not in self.data:
            return -1
        else:
            self.access(key)  
            return self.data[key]

    def put(self, key_pair: tuple):
        key, value = key_pair
        if key in self.data:
            self.data[key] = value
            self.access(key)
            return

        if self.size < self.capacity:
            self.insert_new_key(key, value)
            self.size += 1
        else:
            to_remove = self.head_LRU.next
            self.head_LRU.next = to_remove.next

            del self.data[to_remove.value]
            del self.list_node[to_remove.value]

            self.insert_new_key(key, value)

    def insert_new_key(self, key, value):
        to_insert = Node(key)
        self.data[key] = value
        self.list_node[key] = to_insert

        last_node = self.tail_LRU.prev
        last_node.next = to_insert
        to_insert.prev = last_node
        
        to_insert.next = self.tail_LRU
        self.tail_LRU.prev = to_insert
    
    def access(self, key):
        assert(key in self.data)
        if self.tail_LRU.prev.value != key:
            node = self.list_node[key]
            prev = node.prev
            next  = node.next
            prev.next = next
            next.prev = prev

            last_node = self.tail_LRU.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail_LRU
            self.tail_LRU.prev = node

    def print_cache(self):
        curr = self.head_LRU.next
        while curr != self.tail_LRU:
            print(f'{curr.value}:{self.data[curr.value]} ', end=" ")
            curr = curr.next


x = cache(2)

x.put((1,3))
x.put((2,4))
print(x.get(0)) #return -1
print(x.get(1))  #return 3
x.put((3, 6)) #will evict key 2
print(x.get(2)) #return -1
print(x.get(3)) #return 6

x.print_cache()
