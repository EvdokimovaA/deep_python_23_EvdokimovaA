class CacheNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, limit=42):
        self.limit = limit
        self.dic = {}
        self.head = CacheNode(0, 0)
        self.tail = CacheNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self.__remove_node(n)
            self.__add_node(n)
            return n.val
        return None

    def set(self, key, value):
        if key in self.dic:
            self.__remove_node(self.dic[key])
        new_node = CacheNode(key, value)
        self.__add_node(new_node)
        self.dic[key] = new_node

        if len(self.dic) > self.limit:
            new_node = self.head.next
            self.__remove_node(new_node)
            del self.dic[new_node.key]

    def __remove_node(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def __add_node(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
