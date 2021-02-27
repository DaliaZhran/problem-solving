# https://leetcode.com/problems/lru-cache/


"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
"""


# We use a doubly linkedlist to avoid O(N) delete/shift time
# We use a hashmap to avoid O(N) search time
# Space complexity : O(capacity)
class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node):
        self._delete_node(node)
        self._add_node(node)

    def _add_node(self, node):
        prev_head = self.head.next
        node.prev = self.head
        self.head.next = node

        node.next = prev_head
        prev_head.prev = node

    def _delete_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node == None:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if node == None:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value

            self.cache[key] = new_node
            self._add_node(new_node)  # add node to the doubly LL

            self.size += 1

            if self.size > self.capacity:
                tail = self.tail.prev
                self._delete_node(tail)
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


# 2, Shortest / Using OrderedDict

from collections import OrderedDict


class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
