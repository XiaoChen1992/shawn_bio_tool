"""
@ Description: Sequence one-hot
@ Author: Shawn Chen
@ Date: 2022-01-18
"""

import numpy as np
from read_fasta import read_fasta

def one_hot(fasta_file):
    tokens_dict_msa_trasfomer_order = {'L': 0, 'A': 1, 'G': 2, 'V': 3, 'S': 4, 'E': 5, 'R': 6, 'T': 7, 'I': 8, 'D': 9,
                   'P': 10, 'K': 11, 'Q': 12, 'N': 13, 'F': 14, 'Y': 15, 'M': 16, 'H': 17, 'W': 18,
                   'C': 19, 'X': 20}

    tokens_dict_regular_order = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4,
                'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9,
                'M': 10, 'N': 11, 'P': 12, 'Q': 13,
                'R': 14, 'S': 15, 'T': 16, 'V': 17,
                'W': 18, 'Y': 19, 'X': 20}
    _, length, seq = read_fasta(fasta_file)

    one_hot_array = np.zeros([length, 21])
    
    for idx, item in enumerate(seq.upper()):
        if item not in tokens_dict_msa_trasfomer_order.keys():
            item = 'X'
        col_idx = tokens_dict_msa_trasfomer_order[item]
        one_hot_array[idx, col_idx] = 1

    return one_hot_array
