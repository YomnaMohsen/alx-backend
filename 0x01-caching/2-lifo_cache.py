#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """lifo caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if(item and key):
            if(len(self.cache_data) == self.MAX_ITEMS):
                discardkey = list(self.cache_data.keys())[self.MAX_ITEMS-1]
                del self.cache_data[discardkey]
                print("DISCARD: {}".format(discardkey))
            self.cache_data[key] = item

    def get(self, key):
        """ get an item from the cache
        """
        return self.cache_data.get(key, None)
