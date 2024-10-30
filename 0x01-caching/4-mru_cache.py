#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """mru caching system"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.lrulist_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if(item and key):
            self.cache_data[key] = item
            if key in self.lrulist_keys:
                self.lrulist_keys.remove(key)
            self.lrulist_keys.append(key)    
            if(len(self.cache_data) > self.MAX_ITEMS):
                discardkey = self.lrulist_keys.pop()
                del self.cache_data[discardkey]
                print("DISCARD: {}".format(discardkey))
            

    def get(self, key):
        """ get an item from the cache
        """
        return self.cache_data.get(key, None)
