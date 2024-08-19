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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        '''
        get_p = self.get_page(page, page_size)
        prev_p = page - 1 if page > 1 else None
        total_p = math.ceil(len(self.dataset())/page_size)
        next_p = page + 1 if page < total_p else None
        page_s = 0 if total_p < page else page_size
        return dict(page_size=page_s, page=page, data=get_p,
                    next_page=next_p,  prev_page=prev_p, total_pages=total_p)
