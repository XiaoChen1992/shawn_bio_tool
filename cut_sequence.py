"""
@ Description: Cut sequence with the fixed length and generate the new sub-sequence
@ Author: Shawn Chen
@ Date: 2022-01-11
"""

import os
import sys
from read_fasta import read_fasta


def cut_sequence(input_sequence: str, maximum_length: int) -> None:
    seq = read_fasta(input_sequence)

    if len(seq) <= maximum_length:
        print('This sequence is shorter than maximum length')
        sys.exit(1)

    output_folder, target_id = os.path.split(input_sequence)
    target_id = target_id.split('.')[0]

    sub_seq = [seq[y-maximum_length: y] for y in range(maximum_length, len(seq)+maximum_length, maximum_length)]
    
    for idx, i in enumerate(sub_seq):
        
        with open(f'{output_folder}/{target_id}_sub_{idx}.fasta', 'w') as f:
            f.writelines(f'>{target_id}_sub_{idx} | {len(i)}')
            f.writelines('\n')
            f.writelines(i)

    return None


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError('This function must have two argument. The fasta file and maximum length.')

    input_sequence = sys.argv[1]
    maximum_length = sys.argv[2]
    maximum_length = int(maximum_length)

    if not os.path.isfile(input_sequence):
        raise FileNotFoundError(f'Please chcek the input sequence path {input_sequence}.')

    cut_sequence(input_sequence, maximum_length)
  