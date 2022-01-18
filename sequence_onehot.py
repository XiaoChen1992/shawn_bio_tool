"""
@ Description: Sequence one-hot
@ Author: Shawn Chen
@ Date: 2022-01-18
"""

import numpy as np
from read_fasta import read_fasta

def one_hot(fasta_file):
    tokens_dict = {'L': 0, 'A': 1, 'G': 2, 'V': 3, 'S': 4, 'E': 5, 'R': 6, 'T': 7, 'I': 8, 'D': 9,
                   'P': 10, 'K': 11, 'Q': 12, 'N': 13, 'F': 14, 'Y': 15, 'M': 16, 'H': 17, 'W': 18,
                   'C': 19, 'X': 20}


    _, length, seq = read_fasta(fasta_file)

    one_hot_array = np.zeros([length, 21])
    
    for idx, item in enumerate(seq.upper()):
        if item not in tokens_dict.keys():
            item = 'X'
        col_idx = tokens_dict[item]
        one_hot_array[idx, col_idx] = 1

    return one_hot_array
