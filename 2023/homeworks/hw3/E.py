import sys

MAX_SAMPLES = 10 ** 5


class Node:
    def __init__(self, key=None, val='none', previous=None, next=None):
        self.key = key
        self.val = val
        self.next_node = None
        self.previous = previous
        self.next = next

    def set(self, key, val, previous, next, next_node):
        self.key = key
        self.val = val
        self.previous = previous
        self.next = next
        self.next_node = next_node


class MyLinkedMap:
    def __init__(self, arr_size, a_value=7, p_value=31):
        self.a_value = a_value
        self.p_value = p_value
        self.arr_size = arr_size
        self.hash_arr = [Node() for _ in range(arr_size)]
        self.curr_node = Node(previous=Node())

    def hash_function(self, str_val):
        hash_val = 0
        for char_val in str_val:
            hash_val = (hash_val * self.a_value + ord(char_val)) % self.p_value
        return hash_val % self.arr_size

    def insert(self, key_val, str_val):
        hash_key_val = self.hash_function(key_val)
        inode = self.hash_arr[hash_key_val]
        while True:
            if inode.key is None:
                inode.set(key_val, str_val, previous=self.curr_node, next=Node(), next_node=Node())
                self.curr_node.next = inode
                self.curr_node = inode
                return 'new'
            elif inode.key == key_val:
                inode.val = str_val
                return 'overwrite'
            else:
                inode = inode.next_node

    def delete(self, key_val):
        hash_key_val = self.hash_function(key_val)
        inode = self.hash_arr[hash_key_val]
        if self.curr_node.key == key_val:
            self.curr_node = self.curr_node.previous
        if inode.key == key_val:
            inode.next.previous = inode.previous
            inode.previous.next = inode.next
            self.hash_arr[hash_key_val] = inode.next_node
            return
        while inode.next_node:
            if inode.next_node.key == key_val:
                inode.next_node.previous.next = inode.next_node.next
                inode.next_node.next.previous = inode.next_node.previous
                inode.next_node = inode.next_node.next_node
                return
            else:
                inode = inode.next_node
        return

    def get(self, key_val):
        hash_key_val = self.hash_function(key_val)
        inode = self.hash_arr[hash_key_val]
        while True:
            if inode.key is None:
                return 'none'
            elif inode.key == key_val:
                return inode.val
            else:
                inode = inode.next_node

    def prev(self, key_val):
        hash_key_val = self.hash_function(key_val)
        inode = self.hash_arr[hash_key_val]
        while inode.key != key_val:
            if inode.key is None:
                return 'none'
            inode = inode.next_node
        return inode.previous.val

    def next(self, key_val):
        hash_key_val = self.hash_function(key_val)
        inode = self.hash_arr[hash_key_val]
        while inode.key != key_val:
            if inode.key is None:
                return 'none'
            inode = inode.next_node
        return inode.next.val


size = MAX_SAMPLES * 2
my_map = MyLinkedMap(size, a_value=7, p_value=171723191)
for line in sys.stdin:
    opp = line.split()
    if opp[0] == 'put':
        my_map.insert(opp[1], opp[2])
    elif opp[0] == 'delete':
        my_map.delete(opp[1])
    elif opp[0] == 'get':
        print(my_map.get(opp[1]))
    elif opp[0] == 'prev':
        print(my_map.prev(opp[1]))
    elif opp[0] == 'next':
        print(my_map.next(opp[1]))