
'''
1.Design a complete binary tree ADT based on a singly linked list, assign the first element’s index as 0. Given
an index i, please implement three operations to get its parent, left child, and right child, respectively
'''

class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class ADT:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key):
        newNode = Node(key, None)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def get_parent(self, i):
        if i == 0:
            return None
        else:
            return self.find((i - 1) // 2)

    def get_left_child(self, i):
        return self.find(2 * i + 1)

    def get_right_child(self, i):
        return self.find(2 * i + 2)

    def find_node(self, i):
        if self.head is None:
            return None
        current = self.head
        if i == 0:
            return current
        pos = 0
        while current.next:
            current = current.next
            pos += 1
            if pos == i:
                return current
        return None

    def find(self, i):
        res = self.find_node(i)
        if res:
            return res.key
        else:
            return None


#2
    #based on the code in question 1
    def del_min(self):
        if self.size == 0:
            return None
        retval = self.find(0)
        self.swap(self.head, self.tail)
        self.del_tail()
        self.size -= 1
        self.perc_down(0)
        return retval

    def perc_up(self):
        i = self.size - 1
        while (i - 1) // 2 >= 0:
            node_i = self.find_node(i)
            node_p = self.find_node((i - 1) // 2)
            if node_i.key < node_p.key:
                self.swap(node_p, node_i)
            i = (i - 1) // 2

    def perc_down(self, i):
        while (i * 2 + 1) <= self.size - 1:
            mc_pos = self.find_min_child(i)
            node_mc = self.find_node(mc_pos)
            node_i = self.find_node(i)
            if node_i.key > node_mc.key:
                self.swap(node_i, node_mc)
            i = mc_pos

    def del_tail(self):
        if self.size == 1:
            self.tail = None
            return
        new_tail = self.find_node(self.size - 2)
        new_tail.next = None
        self.tail = new_tail

    def find_min_child(self, i):
        if i * 2 + 2 > self.size - 1:
            return i * 2 + 1
        else:
            if self.get_left_child(i) < self.get_right_child(i):
                return i * 2 + 1
            else:
                return i * 2 + 2

    def swap(ni, nj):
        tmp = nj.key
        nj.key = ni.key
        ni.key = tmp

# a minimum priority queue based on ADT
class PriorityQueue:
    def __init__(self):
        self.heap = ADT()

    def insert(self, k):
        self.heap.insert(k)
        self.heap.perc_up()

    def delMin(self):
        return self.heap.del_min()

#4.	performance benchmark
import random
from priority_queue import PriorityQueue

def insert(k):
    PriorityQueue().insert(k)

def delMin(q):
    q.delMin()

def test_insert(benchmark):
    key = random.randint(1, 100)
    benchmark(insert, key)

def test_delMin(benchmark):
    q = PriorityQueue()
    q.insert(random.randint(1, 100))
    benchmark(delMin, q)


#5

import os
from priority_queue import PriorityQueue
from graphviz import Digraph


def convert_to_digraph(tree):
    dot = Digraph(comment='Tree Structure')
    edges = []
    for i in range(tree.size):
        dot.node(f'{i}', f'{tree.find(i)}')
        lc_pos = 2 * i + 1
        rc_pos = 2 * i + 2
        if lc_pos < tree.size:
            dot.node(f'{lc_pos}', f'{tree.find(lc_pos)}')
            edges.append(f"{i}{lc_pos}")
        if rc_pos < tree.size:
            dot.node(f'{rc_pos}', f'{tree.find(rc_pos)}')
            edges.append(f"{i}{rc_pos}")
    dot.edges(edges)
    return dot


if __name__ == '__main__':
    os.environ['PATH'] = os.pathsep + r'D:\soft\Graphviz\bin'
    q = PriorityQueue()
    data = [9, 5, 6, 2, 3]
    for ele in data:
        q.insert(ele)
    dot_data = convert_to_digraph(q.heap)
    dot_data.render('./Tree-Structure.gv', view=True)


