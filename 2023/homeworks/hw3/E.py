import sys

M = 2 * 10 ** 5
P = 16769023
A = 31


def hash_function(x, capacity):
    res = 0
    for i in reversed(x):
        res = (res * A + ord(i)) % P
    return res % capacity


class Node:
    def __init__(self, data=None, global_prev=None):
        self.data = data
        self.next = None
        self.global_prev = global_prev
        self.global_next = None


class LinkedMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.global_prev = None

    def put(self, data):
        index = hash_function(data, self.capacity)
        if self.arr[index] is None:
            self.arr[index] = Node(data=data, global_prev=self.global_prev)
            if self.global_prev is not None:
                self.global_prev.global_next = self.arr[index]
            self.global_prev = self.arr[index]
            return
        node = self.arr[index]
        while node is not None:
            if node.data == data:
                return
            prev_node = node
            node = node.next
        new_node = Node(data=data, global_prev=self.global_prev)
        self.global_prev.global_next = new_node
        prev_node.next = new_node
        self.global_prev = new_node

    def delete(self, data):
        index = hash_function(data, self.capacity)
        if self.arr[index] is None:
            return
        prev_node = None
        node = self.arr[index]
        while node is not None:
            if node.data == data:
                if node.global_prev is None and node.global_next is None:
                    self.global_prev = None
                elif node.global_next is None:
                    self.global_prev = node.global_prev
                    node.global_prev.global_next = None
                elif node.global_prev is None:
                    node.global_next.global_prev = None
                else:
                    node.global_prev.global_next = node.global_next
                    node.global_next.global_prev = node.global_prev
                if prev_node is None:
                    self.arr[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next

    def get_all(self):
        elements = []
        node = self.global_prev
        while node is not None:
            elements.append(node.data)
            node = node.global_prev
        return elements


class LinkedList:
    def __init__(self, key, capacity):
        self.key = key
        self.linked_map = LinkedMap(capacity)
        self.next = None


class MultiMap:
    def __init__(self):
        self.arr = [None] * M

    def put(self, key, data):
        index = hash_function(key, M)
        if self.arr[index] is None:
            self.arr[index] = LinkedList(key, M // 1000)
            self.arr[index].linked_map.put(data)
            return
        node = self.arr[index]
        while node is not None:
            if node.key == key:
                node.linked_map.put(data)
                return
            prev_node = node
            node = node.next
        new_node = LinkedList(key, M // 1000)
        new_node.linked_map.put(data)
        prev_node.next = new_node

    def get(self, key):
        index = hash_function(key, M)
        if self.arr[index] is None:
            return 0
        node = self.arr[index]
        while node is not None:
            if node.key == key:
                elements = node.linked_map.get_all()
                if len(elements) == 0:
                    return 0
                return str(len(elements)) + ' ' + ' '.join(reversed(elements))
            node = node.next
        return 0

    def delete(self, key, data):
        index = hash_function(key, M)
        node = self.arr[index]
        if node is not None:
            while node is not None:
                if node.key == key:
                    node.linked_map.delete(data)
                    return
                node = node.next

    def delete_all(self, key):
        index = hash_function(key, M)
        if self.arr[index] is None:
            return
        node = self.arr[index]
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.arr[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next


array = MultiMap()
for line in sys.stdin:
    command = line.split()
    if command[0] == "put":
        array.put(command[1], command[2])
    elif command[0] == "get":
        print(array.get(command[1]))
    elif command[0] == "delete":
        array.delete(command[1], command[2])
    elif command[0] == "deleteall":
        array.delete_all(command[1])