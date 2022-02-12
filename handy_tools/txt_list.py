"""
@ Description: Read .txt file and return python list or export list as txt tile
@ Author: Shawn Chen
@ Date: 2022-01-12
"""

from typing import List

def txt_to_list(txt_file: str, pattern='\n') -> List:
    def remove_n(lst: List, pattern='\n') -> List:
        return [i.strip(pattern) for i in lst]

    with open(txt_file, 'r') as f:
        tmp_list = f.readlines()
    tmp_list = remove_n(tmp_list, pattern=pattern)
    return tmp_list


def list_to_txt(lst: List, txt_file: str) -> None:
    with open(txt_file, 'w') as f:
        for i in lst:
            f.writelines(i + '\n')
    return None