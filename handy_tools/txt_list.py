"""
@ Description: Read .txt file and return python list or export list as txt tile
@ Author: Shawn Chen
@ Date: 2022-01-12
"""

from turtle import st
from typing import List, Any

def txt_to_list(txt_file: str, pattern: str = '\n') -> List[Any]:
    def remove_n(lst: List[Any], pattern: str = '\n') -> List[Any]:
        return [i.strip(pattern) for i in lst]

    with open(txt_file, 'r') as f:
        tmp_list = f.readlines()
    tmp_list = remove_n(tmp_list, pattern=pattern)
    return tmp_list


def list_to_txt(lst: List[str], txt_file: str) -> None:
    with open(txt_file, 'w') as f:
        for i in lst:
            f.writelines(i + '\n')
    return None