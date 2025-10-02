from collections import deque
from collections import defaultdict
class DualLinkNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.curcap = 0
        self.head = DualLinkNode()
        self.tail = DualLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = defaultdict()
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head
    def removeNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value

    def put(self, key: int, value: int) -> None:
            node = None
            if key not in self.cache:
                node = DualLinkNode(key, value)
                self.cache[key] = node
                self.addToHead(node)
                if self.curcap == self.cap:
                    key1 = self.removeTail() # evict the least recently used key
                    self.cache.pop(key1.key)
                else:
                    self.curcap += 1

            else:
                node = self.cache[key]
                node.value = value
                self.moveToHead(node)


if __name__ == '__main__':

        actions = input().strip().split()
        numbers = list(map(list, input().strip().split()))
        print(actions)
        print(numbers)
        l1 = None
        for i in range(len(actions)):
            if actions[i] == 'LRUCache':
                l1 = LRUCache(numbers[i])
            print(len(numbers[i]))
            print(int(numbers[i][0]))
            if actions[i] == 'get':
                l1.get(numbers[i])
            if actions[i] == 'put':
                l1.put(numbers[i],)
        #l1.get()
