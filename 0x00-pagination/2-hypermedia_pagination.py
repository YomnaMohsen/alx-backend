#!/usr/bin/env python3
"""helper-fn module"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index
    for the range of indexes for pagination based on the page and page_size.

    Args:
    page_no : int
    page_size: int

    return:
    tuple conatins start and end index(0-based)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get list of pages from dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        data_set = self.dataset()
        total = math.ceil(len(data_set) / page_size)
        prev_page = page - 1 if page - 1 > 0 else None
        next_page = page + 1 if page + 1 < total else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total
        }
