import sys


class Pair:
    def __init__(self, value, key):
        self.value = value
        self.key = key


class Heap:
    def __init__(self):
        self.elements = []
        self.operations = 0
        self.size = 0

    def swap(self, i, j):
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

    def sift_up(self, i):
        while i > 0:
            if self.elements[i].value < self.elements[(i - 1) // 2].value:
                self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 < len(self.elements) - 1:
            cur = self.elements[i].value
            left = self.elements[2 * i + 1].value
            if 2 * i + 2 == len(self.elements) - 1:
                right = float('inf')
            else:
                right = self.elements[2 * i + 2].value
            if left <= right and left < cur:
                self.swap(i, 2 * i + 1)
                i = 2 * i + 1
            elif right < left and right < cur:
                self.swap(i, 2 * i + 2)
                i = 2 * i + 2
            else:
                break

    def add(self, x):
        self.operations += 1
        self.elements.append(Pair(x, self.operations))
        self.sift_up(self.size)
        self.size += 1

    def remove_min(self):
        self.operations += 1
        if self.size == 0:
            return '*'
        res = (self.elements[0].value, self.elements[0].key)
        self.swap(0, self.size - 1)
        self.sift_down(0)
        self.elements.pop()
        self.size -= 1
        return res

    def decrease(self, x, v):
        self.operations += 1
        idx = -1
        for i in range(len(self.elements)):
            if self.elements[i].key == x:
                idx = i
                break
        if idx != -1:
            self.elements[idx].value = v
            self.sift_up(idx)


class PriorityQueue(object):
    def __init__(self):
        self.items = Heap()

    def push(self, x):
        self.items.add(x)

    def pop(self):
        return self.items.remove_min()

    def decrease_key(self, x, v):
        return self.items.decrease(x, v)


pq = PriorityQueue()
for i, line in enumerate(sys.stdin):
    a = line.split()
    n = len(a)
    if n == 2:
        pq.push(int(a[1]))
    elif n == 1:
        print(*pq.pop())
    else:
        pq.decrease_key(int(a[1]), int(a[2]))