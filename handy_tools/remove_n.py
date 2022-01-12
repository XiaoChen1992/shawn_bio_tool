"""
@ Description: iteratively  remove pattern in a list for each element
@ Author: Shawn Chen
@ Date: 2021-01-12
"""

from typing import List


def remove_n(lst: List, pattern='\n') -> List:
    return [i.strip(pattern) for i in lst]
