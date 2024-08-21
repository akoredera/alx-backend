#!usr/bin/env python3
'''0. Basic dictionary'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''inherits from BaseCaching and is a caching system'''
    def __init__(self):
        '''constructor inherit from the base'''
        super().__init__()

    def put(self, key, item):
        '''must assign to the dictionary'''
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            counter = 0
            for k in self.cache_data.keys():
                counter = counter + 1
                if counter == 1:
                    print(f'DISCARD: {k}')
                    self.cache_data.pop(k)
                    break

    def get(self, key):
        '''must return the value in self.cache_data'''
        return self.cache_data.get(key, None)
