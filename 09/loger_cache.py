import argparse
import logging

logger = logging.getLogger('loger_cache')
logger.setLevel(logging.DEBUG)


class SomeFilter(logging.Filter):
    def filter(self, record):
        return len(record.msg.split()) % 2 != 0


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
            logger.info('Was get element %s with key %s', n.val, key)
            return n.val
        logger.warning('Key %s not exist in cache', key)
        return None

    def set(self, key, value):
        if key in self.dic:
            logger.info('Key %s already exist in cache', key)
            self.__remove_node(self.dic[key])
            logger.info('Element %s with key %s was removed from cache', self.dic[key].val, key)
        new_node = CacheNode(key, value)
        logger.info('Create new element %s with key %s in cache', value, key)
        self.__add_node(new_node)
        logger.info('Add element %s with key %s in cache', value, key)
        self.dic[key] = new_node

        if len(self.dic) > self.limit:
            logger.warning('Cache full')
            new_node = self.head.next
            self.__remove_node(new_node)
            logger.info('Element %s with key %s was removed from cache', new_node.val, new_node.key)
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


def set_loggers(stdout_option, filter_option):
    file_handler = logging.FileHandler('cache.log')
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s\t%(name)s\t%(levelname)s\t%(lineno)s\t%(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler()
    file_handler.setLevel(logging.INFO)
    if stdout_option:
        stdout_formatter = logging.Formatter(
            '==%(asctime)s\t%(threadName)s\t%(process)s\t(%(name)s): %(message)s'
        )
        stdout_handler.setFormatter(stdout_formatter)
        logger.addHandler(stdout_handler)

    if filter_option:
        file_handler.addFilter(SomeFilter())
        if stdout_option:
            stdout_handler.addFilter(SomeFilter())


def cache_simulation():
    cache_limit = 10
    cache = LRUCache(cache_limit)
    for i in range(cache_limit+5):
        cache.set(i, f'value{i}')

    for i in range(cache_limit):
        cache.get(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-f', action='store_true')
    args = parser.parse_args()

    set_loggers(args.s, args.f)

    cache_simulation()
