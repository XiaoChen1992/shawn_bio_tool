"""
@ Description: Read spider file generated by SPIDER3-Single_np and return ss3, ss8
@ Author: Shawn
@ Date: 2022-01-11
"""

import pandas as pd


def helper(spider_file: str) -> pd.DataFrame:
    tmp_file = open(spider_file)
    ss3 = []
    ss8 = []
    
    for line in tmp_file:
        tmp_list = line.split(' ')
        ss3.append(tmp_list[2])
        ss8.append(tmp_list[3])

    ss3.pop(0)
    ss8.pop(0)
    tmp_df = pd.DataFrame(list(zip(ss3, ss8)))
    tmp_df.columns = ['ss3', 'ss8']
    return tmp_df
