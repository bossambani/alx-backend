#!/usr/bin/env python3
"""0-simple_helper_function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function named index_range that takes two integer
    arguments page and page_size.

    The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
