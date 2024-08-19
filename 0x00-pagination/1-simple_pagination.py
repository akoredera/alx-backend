#!/usr/bin/env python3
'''
1. Simple pagination
'''
import csv
import math
from typing import List
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        '''
        function named index_range that takes two integer
        arguments page and page_size.
        The function should return a tuple of size two
        containing a start index and an end index corresponding
        to the range of indexes to return in a list for those
        particular pagination parameters.
        '''
        return (page * page_size) - page_size, page * page_size

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        takes two integer arguments page with default value 1 and
        page_size with default value 10.
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset
        (i.e. the correct list of rows). If the input arguments
        are out of range for the dataset, an empty list should be returned.
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        # Get dataset
        dataset = self.dataset()
        # Get index range
        start_index, end_index = Server.index_range(page, page_size)
        # Return the appropriate slice of the dataset
        if start_index >= len(dataset):
            return []  # Page is out of range
        return dataset[start_index:end_index]
