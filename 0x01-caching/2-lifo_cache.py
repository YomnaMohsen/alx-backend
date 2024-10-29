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
            self.cache_data[key] = item
            if(len(self.cache_data) > self.MAX_ITEMS):
                last = len(self.cache_data)
                discardkey = list(self.cache_data.keys())[last-2]
                del self.cache_data[discardkey]
                print("DISCARD: {}".format(discardkey))

    def get(self, key):
        """ get an item from the cache
        """
        return self.cache_data.get(key, None)
