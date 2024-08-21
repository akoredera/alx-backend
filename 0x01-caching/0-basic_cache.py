#!usr/bin/env python3
'''0. Basic dictionary'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''basic Cache class'''


    def put(self, key, item):
        '''must assign to the dictionary'''
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''must return the value in self.cache_data'''
        return self.cache_data.get(key, None)
