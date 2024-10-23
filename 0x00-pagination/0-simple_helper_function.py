#!/usr/bin/env python3
"""helper-fn module"""


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
