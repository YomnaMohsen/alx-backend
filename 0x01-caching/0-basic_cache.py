#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""

    def put(self, key, item):
        """ Add an item in the cache
        """
        if(item and key):
            self.cache_data[key] = item

    def get(self, key, item):
        """ get an item from the cache
        """
        return self.cache_data.get(key, None)
